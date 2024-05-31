import base64
import zlib
import gzip
import lzma
import base58
import os
import sys
os.system("clear")

def decode_base58(model):
    return base58.b58decode(model)

def decode_base64(model):
    return base64.b64decode(model)

def decode_base32(model):
    return base64.b32decode(model)

def decode_base16(model):
    return base64.b16decode(model)

def decode_base85(model):
    return base64.b85decode(model)

def decompress_zlib(model):
    return zlib.decompress(model)

def decompress_gzip(model):
    return gzip.decompress(model)

def decompress_lzma(model):
    return lzma.decompress(model)

def decoder(Devil, model):
    try:
        if Devil == 'base58':
            decoded_model = decode_base58(model)
        elif Devil == 'base64':
            decoded_model = decode_base64(model)
        elif Devil == 'base32':
            decoded_model = decode_base32(model)
        elif Devil == 'base16':
            decoded_model = decode_base16(model)
        elif Devil == 'base85':
            decoded_model = decode_base85(model)
        elif Devil == 'zlib':
            decoded_model = decompress_zlib(model)
        elif Devil == 'gzip':
            decoded_model = decompress_gzip(model)
        elif Devil == 'lzma':
            decoded_model = decompress_lzma(model)
        else:
            print("غير معروف ")
            return None
        
        return decoded_model
    except Exception as e:
        print(f"Decoding error with {Devil}: {e}")
        return None

def main():
    Devil = input("\x1b[1;92m\x1b[38;5;50mName Tool √ خلي اسم الاداة لك = \x1b[1;92m\x1b[38;5;27m[base58, base64, base32, base16, base85, zlib, gzip, lzma] :\x1b[1;92m\x1b[38;5;49m ").strip()
    model = input("Enter the encoded/ اكتب نوع التشفير ال تريد تفكه : ").strip()
    
    decoded_model = decoder(Devil, model)
    
    if decoded_model:
        try:
            exec(decoded_model)
        except Exception as e:
            print(f"Execution error: {e}")
    else:
        print("Failed to decode the model .")

if __name__ == "__main__":
    main()