import psutil
import pandas as pd
import time
import boto3

def coletar_dados():
    dados = []
    for i in range(100):
        uso_cpu = psutil.cpu_percent(interval=None)
        uso_memoria = psutil.virtual_memory().percent

        dados.append({
            uso_cpu,
            uso_memoria
        })
        
        time.sleep(1)

    return dados

def gerar_csv(dados): 
    df = pd.DataFrame(dados, columns=['uso_cpu', 'uso_memoria'])

    arquivo_csv = 'dados.csv'

    df.to_csv(arquivo_csv, index=False)
    return arquivo_csv

def enviar_bucket_raw(arquivo_csv):
    s3 = boto3.client('s3')
    bucket_name = 's3-ranier-raw'
    try:
        s3.upload_file(arquivo_csv, bucket_name, arquivo_csv)
        print(f"Arquivo {arquivo_csv} enviado para o bucket {bucket_name}.")
    except Exception as e:
        print(f"Erro ao enviar o arquivo para o bucket: {e}")

if __name__ == "__main__":
    dados = coletar_dados()
    arquivo_csv = gerar_csv(dados)
    enviar_bucket_raw(arquivo_csv)
    