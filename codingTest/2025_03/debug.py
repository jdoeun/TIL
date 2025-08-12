def solution(ip_addrs, langs, scores):
    # 언어 구분
    def lang_group(lang):
        if lang in ["C", "C++", "C#"]:
            return "C"
        return lang  # Java, Python3, JavaScript는 여기에 해당

    # langs를 grouped_langs로 변환
    grouped_langs = [lang_group(lang) for lang in langs]

    # IP별 참가자 인덱스를 모으는 딕셔너리
    ip_map = {}

    for i, ip in enumerate(ip_addrs):
        # 해당 IP가 처음이라면 빈 리스트
        if ip not in ip_map:
            ip_map[ip] = []
        ip_map[ip].append(i)  # 참가자 번호 ip별 분류

    # 부정참가자 번호 저장용
    cheaters = set()

    for ip, indices in ip_map.items():
        count = len(indices)

        # 조건 1
        if count >= 4:
            cheaters.update(indices)

        # 조건 2
        if count == 3:
            groups = set(grouped_langs[i] for i in indices)
            if len(groups) == 1:
                cheaters.update(indices)

        # 조건 3
        if count == 2:
            a, b = indices

            if grouped_langs[a] == grouped_langs[b] and scores[a] == scores[b]:
                cheaters.update(indices)

    result = len(ip_addrs) - len(cheaters)

    return result

print(solution(
["5.5.5.5", "155.123.124.111", "10.16.125.0", "155.123.124.111", "5.5.5.5", "155.123.124.111", "10.16.125.0", "10.16.125.0"], ["Java", "C++", "Python3", "C#", "Java", "C", "Python3", "JavaScript"], [294, 197, 373, 45, 294, 62, 373, 373]))