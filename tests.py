"""
streams-exercise.tests.py

This file is intentionally written without the benefit of the Python
unittest library. This can be used to demonstrate in-class that unit testing
is a simple concept which benefits from the use of a library, but does not
require it.

Run with `python tests.py`. The return code will be the number of test FAILURES.
"""

import io

from stream_exercise import StreamProcessor


FAILURES = 0


VALUE = "234761640930110349378289194"
EXPECTED = 5
my_stream_processor = StreamProcessor(io.StringIO(VALUE))
RESULT = my_stream_processor.process()

success = RESULT == EXPECTED
FAILURES += (not success)
MESSAGE = "Testing \"{}\", EXPECTED {} got {}. ".format(VALUE, EXPECTED, RESULT)
MESSAGE += "SUCCESS" if success else "FAILURE"
print(MESSAGE)


VALUE = "03050403020309060707070708"
EXPECTED = 10
my_stream_processor = StreamProcessor(io.StringIO(VALUE))
RESULT = my_stream_processor.process()

success = RESULT == EXPECTED
FAILURES += (not success)
MESSAGE = "Testing \"{}\", EXPECTED {} got {}. ".format(VALUE, EXPECTED, RESULT)
MESSAGE += "SUCCESS" if success else "FAILURE"
print(MESSAGE)


VALUE = "3"
EXPECTED = 0
my_stream_processor = StreamProcessor(io.StringIO(VALUE))
RESULT = my_stream_processor.process()

success = RESULT == EXPECTED
FAILURES += (not success)
MESSAGE = "Testing \"{}\", EXPECTED {} got {}. ".format(VALUE, EXPECTED, RESULT)
MESSAGE += "SUCCESS" if success else "FAILURE"
print(MESSAGE)


VALUE = "2347"
EXPECTED = 2
my_stream_processor = StreamProcessor(io.StringIO(VALUE))
RESULT = my_stream_processor.process()

success = RESULT == EXPECTED
FAILURES += (not success)
MESSAGE = "Testing \"{}\", EXPECTED {} got {}. ".format(VALUE, EXPECTED, RESULT)
MESSAGE += "SUCCESS" if success else "FAILURE"
print(MESSAGE)


VALUE = "23478"
EXPECTED = 2
my_stream_processor = StreamProcessor(io.StringIO(VALUE))
RESULT = my_stream_processor.process()

success = RESULT == EXPECTED
FAILURES += (not success)
MESSAGE = "Testing \"{}\", EXPECTED {} got {}. ".format(VALUE, EXPECTED, RESULT)
MESSAGE += "SUCCESS" if success else "FAILURE"
print(MESSAGE)

print("\n\nTest FAILURES: {} ".format(FAILURES))
exit(FAILURES)
