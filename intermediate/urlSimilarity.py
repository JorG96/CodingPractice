'''
You've got tired of fixing your relatives' PCs after they visited some phishing website so you decided to implement a special plug-in for their browsers which will check if the page they are trying to visit is similar to the one in the blacklist.

For that, you've thought of the special algorithm that for two URLs url1 and url2 computes their similarity as following:

Initially their similarity is 0
Then, it is increased by the following rules:
+5, if the same protocol is used in both URLs.
+10, if url1 and url2 have the same address.
+k, if the first k components of path (delimited by /) are exactly the same (and in the same order) between the two URLs.
+1 if for each varNames common between them. Additional +1 if the respective values are equal too.
URLs are given in the following format: protocol://address[(/path)*][?query] (where query = varName=value(&varName=value)*, parts given in [] are optional, and parts in ()* may be repeated several times). Each of the named elements (i.e. protocol, address, path, varName and value) are guaranteed to contain only alphanumeric characters and periods.

Given the two URLs url1 and url2, compute their similarity using the algorithm described above.

Example

For

url1 = "https://codesignal.com/home/test?param1=42&param3=testing&login=admin"
and

url2 = "https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin"
the output should be
urlSimilarity(url1, url2) = 19.

Because these URLs have the same protocols, addresses, first path component (home) and two varNames, with one also having the same value in both of them.
So the resulting similarity is thus 5 + 10 + 1 + 1 + 1 + 1 = 19.
'''

import urllib.parse

def urlSimilarity(url1, url2):
    u1 = urllib.parse.urlparse(url1)
    q1 = urllib.parse.parse_qs(u1.query, keep_blank_values=True)
    p1 = u1.path.split('/')[1:]
    u2 = urllib.parse.urlparse(url2)
    q2 = urllib.parse.parse_qs(u2.query, keep_blank_values=True)
    p2 = u2.path.split('/')[1:]
    score = 0
    if u1.scheme == u2.scheme: score += 5
    if u1.netloc == u2.netloc: score += 10
    path_pairs = zip(p1, p2)
    for a, b in path_pairs:
        if a == b:
            score += 1
        else:
            break
    query_keys_in_common = q1.keys() & q2.keys()
    score += len(query_keys_in_common)
    for key in query_keys_in_common:
        if q1[key] == q2[key]:
            score += 1
    return score