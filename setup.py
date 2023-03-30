# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
from io import open

# def load_requirements(file_list=None):
#     if file_list is None:
#         file_list = ['requirements.txt']
#     if isinstance(file_list, str):
#         file_list = [file_list]
#     requirements = []
#     for file in file_list:
#         with open(file, encoding="utf-8-sig") as f:
#             requirements.extend(f.readlines())
#     return requirements

requirements = []
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except IOError as e:
    print(e)

test_requirements = [
    'tox',
]


def readme():
    with open('doc/doc_en/whl_en.md', encoding="utf-8-sig") as f:
        README = f.read()
    return README


setup(
    name='paddleocr',
    packages=find_packages(),
    package_dir={'paddleocr': ''},
    include_package_data=True,
    author="Pravesh Kaji Budhathoki",
    # entry_points={"console_scripts": ["paddleocr= paddleocr.paddleocr:main"]},
    version="1.0",
    install_requires=requirements,
    license='Apache License 2.0',
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords=[
        'ocr textdetection textrecognition paddleocr crnn east star-net rosetta ocrlite db chineseocr chinesetextdetection chinesetextrecognition'
    ],
    classifiers=[
        'Intended Audience :: Developers', 'Operating System :: OS Independent',
        'Natural Language :: English (Simplified)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ], )
