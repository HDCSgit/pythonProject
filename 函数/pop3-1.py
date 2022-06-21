from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib

msg = Parser().parsestr(msg_content)
