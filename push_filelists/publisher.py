import sys
import pika
import os

# 接続の作成
pika_param = pika.ConnectionParameters(host='k8s00.k8s.hayaworld.local')
connection = pika.BlockingConnection(pika_param)

# チャンネルの作成
channel = connection.channel()

# キューの作成
channel.queue_declare(queue='hello')

###################################

# ファイル一覧Push
#TODO: 標準出力から相対パスを読み込むようにする
try:
    files = os.listdir(os.curdir + '/files')
except FileNotFoundError:
    print("Directory \"files\" Not found. pwd:" + os.curdir, file=sys.stderr)
    sys.exit(1)

# メッセージの送信
for file in files:
    channel.basic_publish(exchange='',
        routing_key='hello',
        body=file)

# 接続終了
channel.close()