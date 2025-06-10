import boto3
from PIL import Image, ImageDraw, ImageFont
import io
import matplotlib.pyplot as plt

bucket = 'mi-bucket-rekognition-2025-05-22'
image_name = 'Penguin.jpg'

s3 = boto3.client('s3', region_name='us-east-1')
rekognition = boto3.client('rekognition', region_name='us-east-1')

response = s3.get_object(Bucket=bucket, Key=image_name)
image_data = response['Body'].read()
image = Image.open(io.BytesIO(image_data))

response = rekognition.detect_labels(
    Image={'S3Object': {'Bucket': bucket, 'Name': image_name}},
    MaxLabels=10,
    MinConfidence=75
)

draw = ImageDraw.Draw(image)

try:
    font = ImageFont.truetype("arial.ttf", 40)  # Fuente tamaño 40 para texto más grande
except:
    font = ImageFont.load_default()

for label in response['Labels']:
    print(f"Etiqueta: {label['Name']}, Confianza: {label['Confidence']:.2f}%")
    if 'Instances' in label:
        for instance in label['Instances']:
            if 'BoundingBox' in instance:
                box = instance['BoundingBox']
                width, height = image.size
                left = box['Left'] * width
                top = box['Top'] * height
                box_width = box['Width'] * width
                box_height = box['Height'] * height

                # Dibujar rectángulo
                draw.rectangle(
                    [(left, top), (left + box_width, top + box_height)],
                    outline='red',
                    width=3
                )

                text = f"{label['Name']} {int(instance['Confidence'])}%"
                bbox = font.getbbox(text)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]

                # Fondo blanco para el texto (para que se lea mejor)
                draw.rectangle(
                    [(left, top), (left + text_width, top + text_height)],
                    fill='white'
                )
                # Texto dentro del cuadro
                draw.text((left, top), text, fill='red', font=font)

plt.figure(figsize=(10,8))
plt.imshow(image)
plt.axis('off')
plt.show()
