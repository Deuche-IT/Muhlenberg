import boto3

# Crear cliente Rekognition
rekognition = boto3.client('rekognition', region_name='us-east-1')

# Ejecutar análisis de etiquetas
response = rekognition.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'mi-bucket-rekognition-2025-05-22',
            'Name': 'Penguin.jpg'
        }
    },
    MaxLabels=10,          # Cantidad máxima de etiquetas a mostrar
    MinConfidence=75       # Confianza mínima (en %)
)

# Mostrar resultados
for label in response['Labels']:
    print(f"Etiqueta: {label['Name']}, Confianza: {label['Confidence']:.2f}%")
