import json
import os
import shutil
import glob
import pathlib


def read_csv(filename, sep=';'):
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(sep)
        for line in f:
            values = line.strip().split(sep)
            single_data = {k: v for k, v in zip(keys, values)}
            yield single_data


def save_data(data, root):  # root = 'games'
    print(data)
    game = data['Games'].replace(' ', '_')  # game = '2016_Summer'
    dirname = os.path.join(root, game)  # dirname = 'games/2016_Summer'
    os.makedirs(dirname, exist_ok=True)

    country = data['Team'].lower().replace(' ', '_')  # 'poland'
    filename = os.path.join(dirname, country + '.yaml')  # 'games/2016_Summer/poland.yaml'
    with open(filename, 'a+') as f:
        row = f'- {json.dumps(data)}\n'
        f.write(row)


def split_file(src_filename, dst_dir='games', remove_if_exist=True):
    if remove_if_exist and os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)

    os.makedirs(dst_dir, exist_ok=True)
    for data in read_csv(src_filename):
        save_data(data, root=dst_dir)


def all_together(src_dir='games', dir_all='_ALL_', remove_if_exist=True):
    dst_dir = os.path.join(src_dir, dir_all)  # eg. dst_dir = 'games/_ALL_'
    if remove_if_exist and os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)

    os.makedirs(dst_dir, exist_ok=True)
    for game in os.listdir(src_dir):  # eg. game = '2016_Summer'
        if game == dir_all:
            continue

        game_dir = os.path.join(src_dir, game)  # eg. game_dir = 'games/2016_Summer'
        for filename in os.listdir(game_dir):  # eg. filename = 'poland.yaml'
            old_path = os.path.join(game_dir, filename)  # eg. old_path = 'games/2016_Summer/poland.yaml'
            print(game, filename)
            country, extension = os.path.splitext(filename)  # eg. country, extension = 'poland', '.yaml'

            new_filename = f'{country}_{game.lower()}{extension}'  # eg. new_filename = 'poland_2016_summer.yaml
            new_path = os.path.join(dst_dir, new_filename)  # eg. new_path = 'games/_ALL_/poland_2016_summer.yaml'

            shutil.copy2(old_path, new_path)


def all_together2(src_dir='games', dir_all='_ALL_', remove_if_exist=True):
    dst_dir = os.path.join(src_dir, dir_all)  # eg. dst_dir = 'games/_ALL_'
    if remove_if_exist and os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)

    os.makedirs(dst_dir, exist_ok=True)
    for file_path in glob.iglob(f'{src_dir}/**/*.yaml', recursive=True):  # eg. file_path = 'games/2016_Summer/poland.yaml'
        print(file_path)
        parts = pathlib.Path(file_path).parts  # eg. parts = ('games', '2016_Summer', 'poland.yaml')
        country, extension = os.path.splitext(parts[-1])  # eg. country, extension = 'poland', '.yaml'
        game = parts[-2]  # eg. game = '2016_Summer'

        new_filename = f'{country}_{game.lower()}{extension}'  # eg. new_filename = 'poland_2016_summer.yaml
        new_path = os.path.join(dst_dir, new_filename)  # eg. new_path = 'games/_ALL_/poland_2016_summer.yaml'

        shutil.copy2(file_path, new_path)


if __name__ == '__main__':
    # split_file(src_filename='box_since_2000.csv')
    all_together2(src_dir='games')
