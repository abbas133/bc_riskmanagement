from cryptography.fernet import Fernet

Key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABctwj_51iq_Sy9PDlO-DDHJp3LZLlF1ToFYtKjuPxg88JFiNEbcqQcp42OAM4-_lJCk8mg5cJz-jc9Uqf1ZBLtXqSdO_b3UuX5larlpDrNueJ72XK_ZyM8Plk4oJoNEmTpfvzFfVErnf5-__LXofajymHRL4EQqZ0VosFIwEeOYjH3jjQ='

def main():
    f = Fernet(Key)
    print(f.decrypt(message))


if __name__ != "__main__":
    main()