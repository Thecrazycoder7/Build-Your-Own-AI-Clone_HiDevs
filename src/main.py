from flask import Flask, render_template, request, jsonify

from flask_cors import CORS
import difflib

app = Flask(__name__)
CORS(app)

# Basic fitness QnA
basic_qna = {
    "hello": "Hi there! Ready to get fit? 💪",
    "hi": "Hey! Ask me your fitness questions!",
    "what is BMI?": "BMI (Body Mass Index) is a measure of body fat based on height and weight.",
    "how to lose belly fat?": "Focus on a balanced diet, regular cardio, and core workouts.",
    "how many steps in a day?": "Aim for at least 8,000 to 10,000 steps per day.",
    "how much water should I drink daily?": "About 2-3 liters a day is good. More if you're working out!",
    "best time to workout?": "Morning is great, but anytime you can stick with is best!",
    "how to gain muscle?": "Eat more protein, lift heavy weights, and rest well.",
    "can I lose weight without gym?": "Yes! Try home workouts, walking, yoga, and a clean diet.",
    "what is HIIT?": "HIIT stands for High Intensity Interval Training — short intense workouts.",
    "how to stay motivated?": "Set small goals, track progress, and reward yourself!",
    "should I workout daily?": "Yes, but give your body rest too. 4-5 days/week is good.",
    "what is protein?": "Protein helps build and repair muscles. Found in eggs, chicken, pulses, etc.",
    "what should I eat before a workout?": "Eat a banana, oats, or something light 30–60 mins before.",
    "how to improve stamina?": "Do cardio like running, swimming, or cycling regularly.",
    "what is calorie deficit?": "Burning more calories than you eat. Key to weight loss.",
    "best exercises for legs?": "Try squats, lunges, step-ups, and leg press.",
    "how to fix back pain?": "Do stretching, posture exercises, and strengthen core muscles.",
    "how to sleep better?": "Avoid screens at night, stay active, and sleep on time.",
    "is yoga good for weight loss?": "Yes! Yoga helps burn fat and reduce stress.",
    "can I drink coffee before workout?": "Yes, it can boost energy and focus.",
    "how many meals per day?": "3 main meals and 1-2 snacks is a good routine.",
    "can I eat rice and lose weight?": "Yes, in moderation with veggies and protein.",
    "how to track calories?": "Use apps like MyFitnessPal or HealthifyMe.",
    "are cheat meals okay?": "Yes, 1–2 per week is fine. Helps avoid cravings.",
    "what is metabolism?": "It’s how your body uses energy. Faster metabolism = burns more calories.",
    "how to tone arms?": "Do push-ups, bicep curls, and tricep dips.",
    "what is clean eating?": "Eating natural, unprocessed food like fruits, veggies, and grains.",
    "can I workout during periods?": "Yes, light exercise helps with cramps and mood.",
    "how long should I workout?": "30–60 minutes a day is great.",
    "what is a good diet plan?": "Balanced meals with carbs, protein, fats, and fiber.",
    "is walking enough?": "Yes, for beginners it's great. Try to increase speed/distance over time.",
    "how to fix posture?": "Stretch daily, avoid slouching, and do back-strengthening exercises.",
    "how much protein per day?": "Around 1g per kg body weight. More if you workout.",
    "can I workout twice a day?": "Yes, if balanced. One intense + one light session is okay.",
    "what are macros?": "Macros are carbs, protein, and fat — the main parts of your diet.",
    "how to do push-ups properly?": "Keep body straight, go slow, and don’t flare elbows too much.",
    "how to reduce stress?": "Workout, meditate, sleep well, and talk to someone.",
    "should I skip breakfast?": "Not always. A healthy breakfast helps start your day right.",
    "how to stay fit at home?": "Do bodyweight exercises, eat clean, and stay active.",
    "can I drink juice daily?": "Fresh juice is okay, but avoid added sugar ones.",
    "best fruit for fitness?": "Bananas, berries, oranges, apples — all are great.",
    "how many hours of sleep?": "7-9 hours daily is needed for recovery and health.",
    "what is DOMS?": "Delayed Onset Muscle Soreness — pain after a tough workout. Normal!",
    "how to warm up?": "Do light jogging, jumping jacks, or dynamic stretches.",
    "should I take supplements?": "Natural food is best. Use supplements only if needed.",
    "how to build abs?": "Eat clean + core workouts like planks and crunches.",
    "are gym machines good?": "Yes, they help beginners with form and safety.",
    "how to stay consistent?": "Make a routine, track it, and stay focused on your goal."
}


# Matching logic
def find_answer(user_input):
    questions = list(basic_qna.keys())
    match = difflib.get_close_matches(user_input.lower(), questions, n=1, cutoff=0.5)
    if match:
        return basic_qna[match[0]]
    return "Sorry, I didn’t get that. Try asking about steps, calories, or fitness tips!"

# Route to handle chatbot requests
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = find_answer(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
