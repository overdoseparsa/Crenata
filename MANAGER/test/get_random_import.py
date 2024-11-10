
import random


class RandomCodeForCSRF():
    data = {

    }
    def __init__(self) -> None:
        self.code = int(
            ''.join(
                [str(random.randint(0,9)) for  number in range(10)]
            )
        )
        RandomCodeForCSRF.data['1'] = self.code

    def get_the_code(self):
        return self.code

    def __str__(self) -> str:
        return str(self.code)

if __name__ =='__main__':
    a = RandomCodeForCSRF()
    print(a.data)
    print(a)
