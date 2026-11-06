import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Картаны баптаймыз (Өлшемі мен шрифтер)
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
ax.axis('off')

# ЭССЕГЕ НЕГІЗДЕЛГЕН МӘТІНДЕР:
sectors = [
    # 1. БАЙЛЫҚ (Sol zhak zhogary) - Эсседен: "Алматыда үлкен үй", "Су жаңа көлік", "Жоғары жалақы"
    {
        "x": 0, "y": 2, "color": "#E066FF", "title": "БАЙЛЫҚ",
        "text": "Алматыдағы үлкен\nжәне әдемі үй\n\nСу жаңа жылдам көлік\n\nЖоғары жалақы"
    },
    # 2. ДАҢҚ (Ortasy zhogary) - Эсседен: "Танымал компания", "Өз ісінің шебері", "Табысты болу"
    {
        "x": 1, "y": 2, "color": "#FF3333", "title": "ДАҢҚ",
        "text": "Үлкен және\nтанымал компания\n\nӨз ісімнің шебері\n\nТабысты болу"
    },
    # 3. МАХАББАТ (On zhak zhogary) - Эсседен: "Сұлу, ақылды жар", "Сыйластық"
    {
        "x": 2, "y": 2, "color": "#FF9999", "title": "МАХАББАТ",
        "text": "Сұлу, ақылды\nжәне мейірімді жар\n\nӨзара сыйластық\n\nМахаббат"
    },
    # 4. ОТБАСЫ (Sol zhak ortasy) - Эсседен: "Үйдегі береке", "Отбасы - маңызды"
    {
        "x": 0, "y": 1, "color": "#99CC33", "title": "ОТБАСЫ",
        "text": "Отбасы — ең\nмаңызды нәрсе\n\nҮйдегі береке\n\nБақытты өмір"
    },
    # 5. ДЕНСАУЛЫҚ / МЕН (Ortasy) - Эсседен: "Салауатты өмір", "Спорт", "Дұрыс тамақтану"
    {
        "x": 1, "y": 1, "color": "#FFFFFF", "title": "ДЕНСАУЛЫҚ (МЕН)",
        "text": "РУСЛАН\n(Осы жерге фото)\n\nСалауатты өмір\nСпортпен шұғылдану\nДұрыс тамақтану"
    },
    # 6. БАЛАЛАР (On zhak ortasy) - Эсседен: "Дені сау балалар", "Тәртіпті"
    {
        "x": 2, "y": 1, "color": "#D4C48C", "title": "БАЛАЛАР",
        "text": "Дені сау балалар\n\nТәртіпті және\nбақытты ұрпақ"
    },
    # 7. БІЛІМ (Sol zhak tomen) - Эсседен: "Университетті жақсы бітіру", "Кітап оқу"
    {
        "x": 0, "y": 0, "color": "#E6CC99", "title": "БІЛІМ",
        "text": "Университетті\nжақсы бітіру\n\nКөп оқу\nжәне еңбек ету\n\nКітап оқу"
    },
    # 8. МАНСАП (Ortasy tomen) - Эсседен: "IT маман", "Компьютермен жұмыс"
    {
        "x": 1, "y": 0, "color": "#6699FF", "title": "МАНСАП",
        "text": "IT маман\n\nКомпьютермен жұмыс\nістеуді ұнату\n\nМақсатқа жету"
    },
    # 9. САЯХАТ (On zhak tomen) - Эсседен: "Шетелге саяхат", "Әдемі қалалар"
    {
        "x": 2, "y": 0, "color": "#A0A0A0", "title": "САЯХАТ",
        "text": "Шетелге саяхат\n\nӘлемнің әдемі\nқалаларында демалу\n\nҚауіпсіз және\nыңғайлы өмір"
    }
]

# Секторларды салу
for sector in sectors:
    rect = patches.Rectangle(
        (sector["x"], sector["y"]), 1, 1,
        linewidth=1, edgecolor='white', facecolor=sector["color"]
    )
    ax.add_patch(rect)

    ax.text(
        sector["x"] + 0.5, sector["y"] + 0.85,
        sector["title"],
        ha='center', va='center', fontsize=14, fontweight='bold', color='black'
    )

    ax.text(
        sector["x"] + 0.5, sector["y"] + 0.5,
        sector["text"],
        ha='center', va='center', fontsize=11, color='black', wrap=True
    )

plt.savefig('Armandar_Kartasy_Final.png', bbox_inches='tight', dpi=300)
print("Сурет дайын: Armandar_Kartasy_Final.png")
plt.show()