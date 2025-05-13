from ragsystem import run_rag
from evaluate import evaluate_answer_quality

def test_configs():
    sample_query = "Why do consumers prefer ai recommendations"
    expected_keywords = ["AI recommendations", "Product type", "AI assistant", "Competence perception", "AI tutor", "Healthcare"]

    print("\n▶️ Test 1: Default config")
    answer = run_rag(sample_query)
    evaluate_answer_quality(answer, expected_keywords)

    print("\n▶️ Test 2: Alternative prompt")
    answer = run_rag(sample_query, use_alternative_prompt=True)
    evaluate_answer_quality(answer, expected_keywords)

    print("\n▶️ Test 3: Second embedding model")
    answer = run_rag(sample_query, model_name="paraphrase-MiniLM-L12-v2")
    evaluate_answer_quality(answer, expected_keywords)

    print("\n▶️ Test 4: With query rewriting")
    answer = run_rag(sample_query, rewrite=True)
    evaluate_answer_quality(answer, expected_keywords)

test_configs()