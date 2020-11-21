""" stream exercise """

import io
# pylint: disable=import-error
# pylint: disable=too-few-public-methods
# pylint: disable=C0103
# The StringIO module an in-memory file-like object
# BYTES_FILE = io.BytesIO(FILE.read().encode('utf8'))
# IO_FILE = io.StringIO(FILE.decode()).read()

FILE1 = io.StringIO("23476164092347616409234761640923476164092347616409234"
                    "761640923476164092347616409234761640923476164092347616"
                    "4092347616409234761640923476164092347616409234761640923"
                    "4761640923476164092347616409234761640923476164092347616"
                    "4092347616409234761640923476164092347616409234761640923"
                    "47616409234761640923476164092347616409234761640923476164"
                    "092347616409234761640923476164092347616409234761640923476"
                    "164092347616409234761640923476164092347616409234761640923"
                    "476164092347616409234761640923476164092347616409234761640"
                    "923476164092347616409")
FILE2 = io.StringIO("2347616409301103493782891942347616409301")
FILE3 = io.StringIO("2347")
FILE4 = io.StringIO("2")


class StreamProcessor(object):
    """process a filestream"""

    def __init__(self, stream):
        self._stream = stream

    def process(self):
        """
        TODO: Implement the `process` method, as described above.
        :return: int
        """

        count = 0  # How many two-digit numbers the `process` method has added together.
        total = 0  # The running total of sums.
        while count < 10 and total < 200:
            digits = self._stream.read(2)
            if len(digits) < 2:
                break
            count += 1
            n = int(digits)
            total += n
        return count


if __name__ == '__main__':
    my_stream_processor1 = StreamProcessor(FILE1)
    my_stream_processor2 = StreamProcessor(FILE2)
    my_stream_processor3 = StreamProcessor(FILE3)
    my_stream_processor4 = StreamProcessor(FILE4)
    print(my_stream_processor1.process())
    print(my_stream_processor2.process())
    print(my_stream_processor3.process())
    print(my_stream_processor4.process())
