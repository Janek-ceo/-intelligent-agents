from transformers import pipeline

qa_pipeline = pipeline("question-answering")

def ask_question(question, context):
    answer = qa_pipeline(question=question, context=context)
    return answer["answer"]

if __name__ == "__main__":
    context = "Sztuczna inteligencja to dziedzina zajmująca się tworzeniem systemów zdolnych do naśladowania ludzkiego myślenia."
    question = "Czym jest sztuczna inteligencja?"
    print(ask_question(question, context))
