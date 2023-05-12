from hello import toyou, add, subtract


def setup_function(function):
    print(" Running Setup: %s " % function.__name__)
    function.x = 10


def teardown_function(function):
    print(" Running Teardown:%s" % function.__name__)
    del function.x