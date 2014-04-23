__author__ = 'arthurnum'


import yaml


class Task():
    def __init__(self, task_number):
        file_name = "tasks/task%d.yaml" % task_number
        stream = open(file_name, 'r')
        data = yaml.load(stream)
        stream.close()
        self.axis_x = data['axis_x']
        self.axis_y = data['axis_y']
        self.start_x = data['start']['x']
        self.start_y = data['start']['y']
        self.drops_count = data['drops']['count']
        self.drops_coords = data['drops']['coords']