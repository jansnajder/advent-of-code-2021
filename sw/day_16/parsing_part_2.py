class Packet:

    def __init__(self, data_binary, offset):
        self.start = offset
        self.version = int(data_binary[offset:offset + 3], 2)
        self.typeid = int(data_binary[offset + 3:offset + 6], 2)
        self.offset = offset + 6
        self.subpackets = []

        if self.typeid == 4:
            self.subpackets.append(self.get_literal(data_binary))
        else:
            self.lentgh_id = self.get_length_id(data_binary)
            if self.lentgh_id == 0:
                self.length_subpackets = self.get_subpackets_info(data_binary, 15)
                self.get_subpackets_from_length(data_binary)
            else:
                self.number_subpackets = self.get_subpackets_info(data_binary, 11)
                self.get_subpackets_from_number(data_binary)

        self.end = self.offset
        self.packet_bits = data_binary[self.start:self.end]

    def get_literal(self, data_binary):
        not_last = 1
        literal_binary = ''

        while not_last:
            not_last = int(data_binary[self.offset], 2)
            self.offset += 1
            literal_binary += data_binary[self.offset:self.offset + 4]
            self.offset += 4

        return int(literal_binary, 2)

    def get_length_id(self, data_binary):
        length_id = int(data_binary[self.offset], 2)
        self.offset += 1
        return length_id

    def get_subpackets_info(self, data_binary, segment_length):
        length = int(data_binary[self.offset:self.offset + segment_length], 2)
        self.offset += segment_length
        return length

    def get_subpackets_from_length(self, data_binary):
        offset = self.offset
        while self.offset < self.length_subpackets + offset:
            self.subpackets.append(Packet(data_binary, self.offset))
            self.offset = self.subpackets[-1].offset

    def get_subpackets_from_number(self, data_binary):
        while len(self.subpackets) < self.number_subpackets:
            self.subpackets.append(Packet(data_binary, self.offset))
            self.offset = self.subpackets[-1].offset

    def get_value(self):
        for idx, subpacket in enumerate(self.subpackets):
            if type(subpacket) is not int:
                self.subpackets[idx] = subpacket.get_value()

        if self.typeid == 0:
            value = sum(self.subpackets)
        elif self.typeid == 1:
            value = 1
            for subpacket in self.subpackets:
                value *= subpacket
        elif self.typeid == 2:
            value = min(self.subpackets)
        elif self.typeid == 3:
            value = max(self.subpackets)
        elif self.typeid == 4:
            value = self.subpackets[0]
        elif self.typeid == 5:
            if self.subpackets[0] > self.subpackets[1]:
                value = 1
            else:
                value = 0
        elif self.typeid == 6:
            if self.subpackets[0] < self.subpackets[1]:
                value = 1
            else:
                value = 0
        elif self.typeid == 7:
            if self.subpackets[0] == self.subpackets[1]:
                value = 1
            else:
                value = 0

        return value


def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data_raw = f.read()

    data_binary = bin(int(data_raw, 16))[2:]
    zeros_to_prepend = (4 - len(data_binary) % 4) % 4
    data_binary = zeros_to_prepend * '0' + data_binary
    return data_binary


if __name__ == '__main__':
    path = 'inputs.txt'
    data_binary = load_data(path)
    offset = 0
    packet = Packet(data_binary, offset)
    packet
    print(packet.get_value())
