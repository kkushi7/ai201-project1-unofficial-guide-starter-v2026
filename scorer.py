def judge(question, expects, answer, results) -> bool:
    return expects.lower().strip() in answer.lower()


# def retrieval_hits(expects, results) -> bool:
#    return any(expects.strip().lower() for chunk in results)
