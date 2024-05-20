import wfuzz
for r in wfuzz.get_payload(range(100)).fuzz(hl=[97], url="http://127.0.0.1:5555/"):
    print(r)