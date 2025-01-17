from azure.servicebus import Message, ServiceBusService


key_name = 'RootManageSharedAccessKey'
key_value = 'Pyh1POvpagtuCZlth3mFiburtkEYQr9M/hJd5Z+JKSA='
service_namespace = 'appForGrid'


class QueueWorker:
    """ Class for working with queues """

    def __init__(self, queue_name):
        """
        Constructor of the QueueWorker class

        :param queue_name: name of the queue
        """

        self.queue_name = queue_name
        self.sbs = ServiceBusService(service_namespace,
                                     shared_access_key_name=key_name,
                                     shared_access_key_value=key_value)

    def create_queue(self):
        """ Function for queue creation """

        self.sbs.create_queue(self.queue_name)

    def send_message(self, message):
        """ Function for sending messages to the queue """

        # Send a message to the queue
        msg = Message(message)
        self.sbs.send_queue_message(self.queue_name, msg)

    def receive_message(self):
        """ Function for receiving messages from the queue """

        # Receive the message from the queue
        msg = self.sbs.receive_queue_message(self.queue_name, peek_lock=False)
        return msg.body.decode("utf-8").replace("'", '"')
