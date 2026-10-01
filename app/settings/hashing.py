import string

from passlib.context import CryptContext

pwd_cntx = CryptContext(
  schemes=['bcrypt'], deprecated='auto'
)

class Encrypt():
  @staticmethod
  def hash_string(string):
    return pwd_cntx.hash(string)