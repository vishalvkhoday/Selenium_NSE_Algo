import pymqi
import logging
queue_manager = "QM01"
channel = "CLIENT.CCBMQMZ4"
host = "AS03R06"
port = "5060"
queue_name = "CCBMQMZ4"
message = "Hello from Python!"
conn_info = "%s(%s)" % (host, port)

qmgr = pymqi.connect(queue_manager, channel, conn_info)
logging.INFO()
queue = pymqi.Queue(qmgr, queue_name)
message = queue.get()
queue.close()

qmgr.disconnect()