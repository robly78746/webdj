#
# import the CryptContext class, used to handle all hashing...
#
from passlib.context import CryptContext

#
# create a single global instance for your app...
#
pwd_context = CryptContext(
    schemes=["sha512_crypt" ],
    default="sha512_crypt",
    )