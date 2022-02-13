from email.base64mime import body_decode
import pika
import time

# 受信時コールバック関数
def callback(ch, method, properties, body):
    print(body.decode('utf-8'))
    ch.basic_ack(delivery_tag = method.delivery_tag)

# 接続の作成
pika_param = pika.ConnectionParameters(host='k8s00.k8s.hayaworld.local')
connection = pika.BlockingConnection(pika_param)

# チャンネルの作成
channel = connection.channel()

# キューの作成
channel.queue_declare(queue='hello')

# 受信
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='hello',on_message_callback=callback)
channel.start_consuming()

# 接続終了
channel.close()

