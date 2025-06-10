import json

def validate(slots):
    if not slots['Location'] or not slots['Location'].get('value'):
        return {
            'isValid': False,
            'violatedSlot': 'Location'
        }

    if not slots['CheckInDate'] or not slots['CheckInDate'].get('value'):
        return {
            'isValid': False,
            'violatedSlot': 'CheckInDate'
        }

    if not slots['Nights'] or not slots['Nights'].get('value'):
        return {
            'isValid': False,
            'violatedSlot': 'Nights'
        }

    if not slots['RoomType'] or not slots['RoomType'].get('value'):
        return {
            'isValid': False,
            'violatedSlot': 'RoomType'
        }

    return {'isValid': True}

def lambda_handler(event, context):
    print("EVENT:\n", json.dumps(event))

    # Seguridad: verificar que 'sessionState' existe
    if 'sessionState' not in event or 'intent' not in event['sessionState']:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing sessionState or intent in event')
        }

    intent = event['sessionState']['intent']['name']
    slots = event['sessionState']['intent']['slots']
    invocation_source = event['invocationSource']

    # Si la invocación es para validación del diálogo
    if invocation_source == 'DialogCodeHook':
        validation_result = validate(slots)
        if not validation_result['isValid']:
            return {
                "sessionState": {
                    "dialogAction": {
                        "type": "ElicitSlot",
                        "slotToElicit": validation_result['violatedSlot']
                    },
                    "intent": {
                        "name": intent,
                        "slots": slots,
                        "state": "InProgress"
                    }
                },
                "messages": [{
                    "contentType": "PlainText",
                    "content": f"Could you please provide your {validation_result['violatedSlot']}?"
                }]
            }

        # Si está todo validado correctamente, seguir
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Delegate"
                },
                "intent": {
                    "name": intent,
                    "slots": slots,
                    "state": "InProgress"
                }
            }
        }

    # Si la invocación es para fulfillment (cumplir la acción)
    elif invocation_source == 'FulfillmentCodeHook':
        location = slots['Location']['value']['interpretedValue']
        nights = slots['Nights']['value']['interpretedValue']
        room_type = slots['RoomType']['value']['interpretedValue']
        check_in = slots['CheckInDate']['value']['interpretedValue']

        message = f"Your reservation for a {room_type} room in {location} for {nights} night(s) starting {check_in} has been confirmed."

        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": intent,
                    "slots": slots,
                    "state": "Fulfilled"
                }
            },
            "messages": [{
                "contentType": "PlainText",
                "content": message
            }]
        }

    # Fallback en caso de error inesperado
    return {
        'statusCode': 400,
        'body': json.dumps('Unexpected invocationSource')
    }
