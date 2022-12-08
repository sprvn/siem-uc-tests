"""Test cases for the fetch hosts script."""

import unittest


from loggen import gen_timestamp, gen_ssh_failure


class FunctionsTest(unittest.TestCase):
    """
    Test functions from the functions directory.
    """

    def setUp(self):
        """
        Create inital list of hosts.
        """

    def test_gen_timestamp(self):
        """
        Test generation of timestamp.
        """
        self.assertEqual("Aug 30 12:54:19", gen_timestamp(1535626459.9408028))

    def test_create_message(self):
        """
        Test if a message is generated as expected.
        """
        self.assertEqual(
            "<86>Aug 30 12:54:19 192.168.10.33 sshd[9033]: Failed password for myuser from 127.0.0.1 port 22 ssh2",
            gen_ssh_failure(
                date=gen_timestamp(1535626459.9408028),
                log_source="192.168.10.33",
                ssh_user="myuser")
        )



if __name__ == '__main__':
    unittest.main()
