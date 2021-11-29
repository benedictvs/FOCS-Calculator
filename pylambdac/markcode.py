# Copyright 2018 Paul Crowley

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import mistletoe
from mistletoe.block_token import BlockCode
from mistletoe.span_token import RawText

def extract_blockcode(b, node):
    if b and node.__class__ == RawText:
        yield node.content
    elif node.__class__ == BlockCode:
        b = True
    if hasattr(node, 'children'):
        for subnode in node.children:
            yield from extract_blockcode(b, subnode)

def blockcodes_as_string(fp):
    return "".join(extract_blockcode(False, mistletoe.Document(fp)))
