import base64

## Decode base16
def decode16(message):
    try:
        decoded_message = base64.b16decode(message)
        return decoded_message
    except:
        return False

## Decode base32
def decode32(message):
    try:
        decoded_message = base64.b32decode(message)
        return decoded_message
    except:
        return False

## Decode base64
def decode64(message):
    try:
        decoded_message = base64.b64decode(message)
        return decoded_message
    except:
        return False

## Try decoding with all
def decode_all(message):
    decoded_message = message
    while True:
        last = decoded_message
        decoded_message = decode16(last)

        if decoded_message:
            continue
        else:
            decoded_message = decode32(last)

        if decoded_message:
            continue
        else:
            decoded_message = decode64(last)
        
        if decoded_message:
            try:
                decoded_message.decode("utf-8")
                continue
            except:
                decoded_message = last
                break
        else:
            decoded_message = last
            break
        
    return decoded_message

## Decode loop
def decode(message, base):
    decoded_message = message
    if base == "16":
        while decoded_message:
            last = decoded_message
            decoded_message = decode16(last)

    elif base == "32":
        while decoded_message:
            last = decoded_message
            decoded_message = decode32(last)

    elif base == "64":
        while decoded_message:
            last = decoded_message
            decoded_message = decode64(last)

    return(last)
    

def interface(message):
    print("What base decoding to choose?")
    print("base16(1), base32(2), base64(3), try all(risky)(4)")
    decode_type = input()
    while decode_type not in ["1", "2", "3", "4"]:
        print("You need to type in 1,2,3 or 4")
        decode_type = input()

    if decode_type == "1":
        decoded_message = decode(message, "16")
    elif decode_type == "2":
        decoded_message = decode(message, "32")
    elif decode_type == "3":
        decoded_message = decode(message, "64")
    elif decode_type == "4":
        decoded_message = decode_all(message)

    return decoded_message



def main():
    while True:
        print("What would you like to decode?")
        print("File(1)")
        print("String(2)")
        to_decode = input().lower()
        
        while to_decode not in ["1", "2", "file", "string"]:
            print("You need to choose: File(1) or String (2)")
            to_decode = input().lower()

        if to_decode == "file":
            to_decode = "1"
        elif to_decode == "string":
            to_decode = "2"
        
        if to_decode == "1":
            while True:
                print("Insert path:")
                path = input()
                try:
                    with open(path) as file:
                        message  = file.read()
                        decoded_message = interface(message)
                        return decoded_message
                except:
                    print("Path does not exist")

        elif to_decode == "2":
            print("Inster string: ")
            string = input()
            decoded_message = interface(string)
            return decoded_message




        


if __name__ == "__main__":
    print(main().decode("utf-8"))