import base64
import zlib
from urllib.parse import quote, unquote


def decode(encoded: str) -> str:
    b64 = base64.b64decode(encoded)
    decompress_obj = zlib.decompressobj(-zlib.MAX_WBITS)
    uri_encoded = decompress_obj.decompress(b64)

    return unquote(uri_encoded)


def encode(decoded: str) -> str:
    quoted = quote(decoded)
    compress_obj = zlib.compressobj(method=zlib.DEFLATED, wbits=-zlib.MAX_WBITS)
    compressed = compress_obj.compress(quoted.encode())
    compressed += compress_obj.flush()
    return base64.b64encode(compressed).decode()
