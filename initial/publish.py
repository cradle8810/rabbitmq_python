import pika

# 接続の作成
pika_param = pika.ConnectionParameters(host='k8s00.k8s.hayaworld.local')
connection = pika.BlockingConnection(pika_param)

# チャンネルの作成
channel = connection.channel()

# キューの作成
channel.queue_declare(queue='hello')

###################################

# メッセージの送信
for i in range(1,100):
    channel.basic_publish(exchange='',
        routing_key='hello',
        body="Message: " + str(i))

# 接続終了
channel.close()