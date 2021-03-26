#!/usr/bin/env python


def and_gate(instruction: str, wires: dict) -> int:
    wire_one, wire_two = instruction.split("AND")
    if wire_one.isdigit() and wire_two.isdigit():
        return int(wire_one) & int(wire_two)
    elif wire_one.isdigit() and wire_two in wires:
        return int(wire_one) & wires[wire_two]
    elif wire_two.isdigit() and wire_one in wires:
        return wires[wire_one] & wire_two
    elif wire_one in wires and wire_two in wires:
        return wires[wire_one] & wires[wire_two]


def or_gate(instruction: str, wires: dict) -> int:
    wire_one, wire_two = instruction.split('OR')
    if wire_one.isdigit() and wire_two.isdigit():
        return int(wire_one) | int(wire_two)
    elif wire_one.isdigit() and wire_two in wires:
        return int(wire_one) | wires[wire_two]
    elif wire_two.isdigit() and wire_one in wires:
        return wires[wire_one] | wire_two
    elif wire_one in wires and wire_two in wires:
        return wires[wire_one] | wires[wire_two]


def lshift_gate(instruction: str, wires: dict) -> int:
    shift_wire, offset = instruction.split('LSHIFT')
    if shift_wire in wires:
        return wires[shift_wire] << int(offset)


def rshift_gate(instruction: str, wires: dict) -> int:
    shift_wire, offset = instruction.split('RSHIFT')
    if shift_wire in wires:
        return wires[shift_wire] >> int(offset)


def not_gate(instruction: str, wires: dict) -> int:
    not_wire = instruction.split("NOT")[1].strip()
    if not_wire in wires:
        return ~int(wires[not_wire])


def work_through_line(line: str, wires: dict, part_two: bool) -> bool:
    instruction, wire = [i.strip().replace(" ", "") for i in line.split("->")]
    if wire != "b" or not part_two:
        if 'AND' in instruction:
            res = and_gate(instruction, wires)
        elif 'OR' in instruction:
            res = or_gate(instruction, wires)
        elif 'LSHIFT' in instruction:
            res = lshift_gate(instruction, wires)
        elif 'RSHIFT' in instruction:
            res = rshift_gate(instruction, wires)
        elif 'NOT' in instruction:
            res = not_gate(instruction, wires)
        elif instruction.isdigit():
            res = int(instruction.strip())
        else:
            if instruction not in wires:
                return False
            res = wires[instruction]

        if res is None:
            return False

        wires[wire] = res if res >= 0 else 65535 + res + 1
        return True


def process_instructions(instructions: list, wires: dict, delayed: list, part_two: bool):
    for inst in instructions:
        if not work_through_line(inst, wires, part_two):
            delayed.append(inst)
    change = True
    while change:
        change = False
        for inst in delayed:
            if work_through_line(inst, wires, part_two):
                change = True
                delayed.remove(inst)


if __name__ == '__main__':
    with open('in7.txt', 'r') as file:
        data = file.readlines()

    wire_dict = {}
    delayed_instructions = []

    process_instructions(data, wire_dict, delayed_instructions, False)
    p1 = wire_dict["a"]
    assert p1 == 3176
    print("p1:", p1)

    wire_dict = {"b": p1}
    process_instructions(data, wire_dict, delayed_instructions, True)
    p2 = wire_dict["a"]
    assert p2 == 14710
    print("p2:", p2)
