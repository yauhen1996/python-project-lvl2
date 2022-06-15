def diff(file1, file2):
    d = {}
    data = {*file1, *file2}
    for key in sorted(data):
        if key in file1 and key not in file2:
            d[key] = {
                "type": "deleted",
                "value": file1[key],
                "children": 0
            }
        elif key in file2 and key not in file1:
            d[key] = {
                "type": "added",
                "value": file2[key],
                "children": 0
            }
        elif file1[key] == file2[key]:
            d[key] = {
                "type": "unchanged",
                "value": file1[key],
                "children": 0
            }
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            d[key] = {
                "type": "nested",
                "value": 0,
                "children": diff(file1[key], file2[key])
            }
        else:
            d[key] = {
                "type": "changed",
                "value_1": file1[key],
                "value_2": file2[key],
                "children": 0
            }
    return d
