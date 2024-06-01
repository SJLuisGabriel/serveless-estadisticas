import json
import statistics

def lambda_handler(event, context):
    
    operation = event['operation']
    if operation == 'media':
        return calcular_media(event, context)
    elif operation == 'mediana':
        return calcular_mediana(event, context)
    elif operation == 'moda':
        return calcular_moda(event, context)
    elif operation == 'varianza':
        return calcular_varianza(event, context)
    elif operation == 'desviacion_estandar':
        return calcular_desviacion_estandar(event, context)
    elif operation == 'rango':
        return calcular_rango(event, context)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Operación no válida.'})
        }

def calcular_media(event, context):
    data = json.loads(event['body'])
    numeros = data['numeros']
    if len(numeros) < 20:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Se requieren al menos 20 valores.'})
        }
    media = sum(numeros) / len(numeros)
    return {
        'statusCode': 200,
        'body': json.dumps({'media': media})
    }

def calcular_mediana(event, context):
    data = json.loads(event['body'])
    numeros = data['numeros']
    if len(numeros) < 20:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Se requieren al menos 20 valores.'})
        }
    mediana = statistics.median(numeros)
    return {
        'statusCode': 200,
        'body': json.dumps({'mediana': mediana})
    }

def calcular_moda(event, context):
    data = json.loads(event['body'])
    numeros = data['numeros']
    if len(numeros) < 20:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Se requieren al menos 20 valores.'})
        }
    try:
        moda = statistics.mode(numeros)
    except statistics.StatisticsError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'No existe una única moda.'})
        }
    return {
        'statusCode': 200,
        'body': json.dumps({'moda': moda})
    }

def calcular_varianza(event, context):
    data = json.loads(event['body'])
    numeros = data['numeros']
    if len(numeros) < 20:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Se requieren al menos 20 valores.'})
        }
    varianza = statistics.variance(numeros)
    return {
        'statusCode': 200,
        'body': json.dumps({'varianza': varianza})
    }

def calcular_desviacion_estandar(event, context):
    data = json.loads(event['body'])
    numeros = data['numeros']
    if len(numeros) < 20:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Se requieren al menos 20 valores.'})
        }
    desviacion_estandar = statistics.stdev(numeros)
    return {
        'statusCode': 200,
        'body': json.dumps({'desviacion_estandar': desviacion_estandar})
    }

def calcular_rango(event, context):
    data = json.loads(event['body'])
    numeros = data['numeros']
    if len(numeros) < 20:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Se requieren al menos 20 valores.'})
        }
    rango = max(numeros) - min(numeros)
    return {
        'statusCode': 200,
        'body': json.dumps({'rango': rango})
    }
