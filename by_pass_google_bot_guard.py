import base64
import random


class ByPassGoogleBotGuard(object):
    size = 2268

    def generate_random_num(self, range_val):
        rand_num = ""
        for i in range(range_val):
            gen_rand_num = random.randint(1, 9)
            rand_num += str(gen_rand_num)
        return int(rand_num)

    def generate_bg_list_array(self):
        bg_list = []
        gen_l = 2
        i = 0
        while i <= self.size:
            bg_list.append(self.generate_random_num(gen_l))
            if gen_l == 2:
                gen_l = 3
            elif gen_l == 3:
                gen_l = 2
            i += 1
        return bg_list

    def generate_bg_request_data(self):
        bg_list = self.generate_bg_list_array()
        bg_uni = ''.join(map(chr, bg_list))
        bg_b64 = base64.b64encode(bg_uni.encode())
        bg_request_data = "!{}".format(bg_b64.decode().replace("+", "-").replace("/", "_").replace("=", ""))
        return bg_request_data


if __name__ == '__main__':
    print(ByPassGoogleBotGuard().generate_bg_request_data())
