
function getCookie(c_name) {
        if(document.cookie.length > 0) {
            let c_start = document.cookie.indexOf(c_name + "=");
            if(c_start != -1) {
                c_start = c_start + c_name.length + 1;
                let c_end = document.cookie.indexOf(";", c_start);
                if(c_end === -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }


function send_result(result, test_number) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', location.href, true);
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));

    if (xhr.readyState === 4) {
        if (xhr.status === 200) {
            console.log("Status 200");
        } else {
            console.log("Error");
        }
    }

    let body = new FormData();
    body.append('result', result.toLowerCase());
    body.append('test_number', test_number);
    xhr.send(body);
}


function readTextFile(filename)
{
    let file = "/static/" + filename;
    let text = "";
    let rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status === 0)
            {
                text = rawFile.responseText;
            }
        }
    };
    rawFile.send(null);
    return text;
}



function results_test_1(args, test_number) {
    document.getElementById("result_field").innerHTML = readTextFile('ResultsTexts/Lesson_1/Lesson_1.txt')

}


function results_test_2(args, test_number) {
    let extra_intro_1_9 = "<div>" + readTextFile("ResultsTexts/Lesson_2/Extra_Intro_1_9.txt") + "</div>";
    let extra_intro_10_14 = "<div>" + readTextFile("ResultsTexts/Lesson_2/Extra_Intro_10_14.txt") + "</div>";
    let extra_intro_15_24 = "<div>" + readTextFile("ResultsTexts/Lesson_2/Extra_Intro_15_24.txt") + "</div>";
    let neuroticism_1_9 = "<div>" + readTextFile("ResultsTexts/Lesson_2/Neuroticism_1_9.txt") + "</div>";
    let neuroticism_10_14 = "<div>" + readTextFile("ResultsTexts/Lesson_2/Neuroticism_10_14.txt") + "</div>";
    let neuroticism_15_24 = "<div>" + readTextFile("ResultsTexts/Lesson_2/Neuroticism_15_24.txt") + "</div>";
    let Choleric = "<div>" + readTextFile("ResultsTexts/Lesson_2/Choleric.txt") + "</div>";
    let Phlegmatic = "<div>" + readTextFile("ResultsTexts/Lesson_2/Phlegmatic.txt") + "</div>";
    let Sanguine = "<div>" + readTextFile("ResultsTexts/Lesson_2/Sanguine.txt") + "</div>";
    let Melancholic = "<div>" + readTextFile("ResultsTexts/Lesson_2/Melancholic.txt") + "</div>";
    let afterwords = "<div>" + readTextFile("ResultsTexts/Lesson_2/Afterwords.txt") + "</div>";
    let last_paragraph = "<div>" + readTextFile("ResultsTexts/Lesson_2/Last_paragraph.txt") + "</div>";


    const extra_intro_points = args.extra_intro;
    const lying_points = args.lying;
    const neuro_points = args.neuroticism;
    let Temperaments = {1:"Холерик", 2:"Меланхолик", 3:"Флегматик", 4:"Сангвиник" };
    let type_start_phrase = "Твой преобладающий тип темперамента - ";
    let final_content = "";
    let test_result;
    // Определение по баллам
    let result_field = document.getElementById("result_field");
    if (extra_intro_points <= 9) final_content += extra_intro_1_9;
    if ((extra_intro_points >= 10) && (extra_intro_points <= 14)) final_content += extra_intro_10_14;
    if (extra_intro_points >= 15) final_content += extra_intro_15_24;
    if (neuro_points <= 9) final_content += neuroticism_1_9;
    if ((neuro_points >= 10) && (neuro_points <= 14)) final_content += neuroticism_10_14;
    if (neuro_points >= 15) final_content += neuroticism_15_24;
    // Определение по кругу
    if ((extra_intro_points >= 12 ) && (neuro_points >= 12)){
        final_content += type_start_phrase + Temperaments["1"] + Choleric;
        test_result = Temperaments["1"];
    }
    if ((extra_intro_points <= 12 ) && (neuro_points >= 12)){
        final_content += type_start_phrase + Temperaments["2"] + Melancholic;
        test_result = Temperaments["2"];
    }
    if ((extra_intro_points <= 12 ) && (neuro_points <= 12)){
        final_content += type_start_phrase + Temperaments["3"] + Phlegmatic;
        test_result = Temperaments["3"];
    }
    if ((extra_intro_points >= 12 ) && (neuro_points <= 12)){
        final_content += type_start_phrase + Temperaments["4"] + Sanguine;
        test_result = Temperaments["4"];
    }
    final_content += afterwords + last_paragraph;
    result_field.innerHTML = final_content;
    send_result(test_result, test_number);
}


function results_test_3(args, test_number) {
    let final_content = "";
    let physical_aggression = "<div>Физическая агрессия - " + args.physical_aggression + "</div>";
    let physical_aggression_text = "<div>" + readTextFile("ResultsTexts/Lesson_3/Physical_aggression_text.txt")+ "</div>";
    let indirect_aggression = "<div>Косвенная агрессия - " + args.indirect_aggression +"</div>";
    let indirect_aggression_text = "<div>" + readTextFile("ResultsTexts/Lesson_3/Indirect_aggression_text.txt")+ "</div>";
    let irritation = "<div>Раздражение - " + args.irritation +"</div>";
    let irritation_text = "<div>" + readTextFile("ResultsTexts/Lesson_3/Irritation_text.txt")+ "</div>";
    let negativism = "<div>Неготивизм - " + args.negativism +"</div>";
    let negativism_text = "<div>" + readTextFile("ResultsTexts/Lesson_3/Negativism_text.txt")+ "</div>";
    let offence = "<div>Обидчивость - " + args.offence +"</div>";
    let offence_text = "<div>" + readTextFile("ResultsTexts/Lesson_3/Offence_text.txt")+ "</div>";
    let suspicion = "<div>Подозрительность - " + args.suspicion +"</div>";
    let suspicion_text = "<div>" + readTextFile("ResultsTexts/Lesson_3/Suspicion_text.txt")+ "</div>";
    let verbal_aggression = "<div>Вербальная агрессия - " + args.verbal_aggression +"</div>";
    let verbal_aggression_text = "<div>" + readTextFile("ResultsTexts/Lesson_3/Verbal_aggression_text.txt")+ "</div>";
    let remorse_conscience = "<div>Угрызения совести / чувство вины  - " + args.remorse_conscience +"</div>";
    let remorse_conscience_text = "<div>" + readTextFile("ResultsTexts/Lesson_3/Remorse_conscience_text.txt")+ "</div>";

    final_content += physical_aggression + physical_aggression_text + indirect_aggression + indirect_aggression_text + irritation + irritation_text + negativism + negativism_text + offence + offence_text + suspicion + suspicion_text + verbal_aggression + verbal_aggression_text + remorse_conscience + remorse_conscience_text;


    let result_field = document.getElementById("result_field");
    result_field.innerHTML =final_content;
    let test_result = "";
    if ((parseInt(args.physical_aggression, 10) > 50) || (parseInt(args.indirect_aggression , 10) > 50) || (parseInt(args.verbal_aggression, 10) > 50))
    {
        test_result = "агрессия"
    }
    else
    {
        test_result = "NO"
    }
    send_result(test_result, test_number)
}


function results_test_4(args, test_number) {
    let final_content = "";
    let types_dict = {"P_D": "Предметно действенное мышление",
                       "A_C": "Абстрактно символическое мышление",
                       "C_L": "Словесно логическое мышление",
                       "H_O": "Наглядно образное мышление",
                       "K": "Креативность"};
    let P_D_text = "<div>Предметно–действенное мышление - " + args.P_D + " баллов из 8</div>";
    let A_C_text = "<div>Абстрактно–символическое мышление - " + args.A_C + " баллов из 8</div>";
    let C_L_text = "<div>Словесно–логическое мышление - " + args.C_L + " баллов из 8</div>";
    let H_O_text = "<div>Наглядно–образное мышление-  " + args.H_O + " баллов из 8</div>";
    let K_text = "<div>Креативность - " + args.K + " баллов из 8</div>";

    let _max = 0;
    let _type = "";
    for(let _key in args){
        if (args[_key] > _max){
            _max = args[_key];
            _type = _key;
        }
    }

    send_result(types_dict.get(_type), test_number);
    final_content += P_D_text + A_C_text + C_L_text + H_O_text + K_text;
    let result_field = document.getElementById("result_field");
    console.log(final_content);
    result_field.innerHTML = final_content;
}


function results_test_5(args, test_number){
    function strength(value){
        if (value <= 3) return "слабо";
        if (value >= 7) return "сильно";
        if ((value >= 4) && (value<=6)) return "средне"
    }

    let _types_dict = {"A":"Артистичный", "P":"Предпринимательский", "O":"Оффисный", "I":"интеллектуальный", "C":"социальный", "R":"реалистичный"};

    let real = "<div>" + "Реалистичный тип - " + args.R/10 * 100 + "%" + " , выражен " + strength(args.R) + "</div>";
    let intellectual = "Интеллектуальный тип - " + args.I /10 * 100 + "%" + " , выражен " + strength(args.I) + "</div>";
    let social = "Социальный тип - " + args.C /10 * 100 + "%" + " , выражен " + strength(args.C) + "</div>";
    let office = "Оффисный тип - " + args.O /10 * 100 + "%" + " , выражен " + strength(args.O) + "</div>";
    let predpr = "Предпринимательский тип - " + args.P /10 * 100 + "%" + " , выражен " + strength(args.P) +  "</div>";
    let artistic = "Артистичный тип - " + args.A /10 * 100 + "%" + " , выражен " + strength(args.A) + "</div>";
    let text = "<div>" + readTextFile("ResultsTexts/Lesson_5/final_content.txt")+ "</div>";
    let final_content = real + intellectual + social + office + predpr + artistic + text;
    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;

    let _max = 0;
    let _type = "";
    for(let _key in args){
        if (args[_key] > _max){
            _max = args[_key];
            _type = _key;
        }
    }

    send_result(_types_dict.get(_type), test_number);
}


function results_test_6(args, test_number) {
    let final_content = "";
    let test_result;
    final_content += "Вы набрали " + args.points + " баллов" + "<br>";
    if (args.points >= 21){
        test_result = "способности";
    }
    else test_result ="no";

    send_result(test_result, test_number)
    final_content += "<div>" + readTextFile("ResultsTexts/Lesson_6/Final_content.txt")+ "</div>";
    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;
}


function results_test_7(args, test_number) {
    let final_content = "";
    let test_result;
    final_content += "Вы ответили верно на " + args.percentage + "вопросов <br>";
    final_content += "<div>" + readTextFile("ResultsTexts/Lesson_7/Final_content.txt")+ "</div>";
    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;
    if (args.percentage >= 50){
        test_result = "способность";
    }
    else
        test_result = "no";
    send_result(test_result, test_number)
}


function results_test_8(args, test_number){
    let final_content = "";
    let test_result;
    final_content += "Вы ответили верно на " + args.percentage + " вопросов<br>";
    final_content += "<div></div>";
    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;

    if (args.percentage >= 50){
        test_result = "образное";
    }
    else
        test_result = "no";
    send_result(test_result, test_number)
}

function results_test_9(args, test_number){
    let final_content = "";
    let test_result;
    final_content += "Вы ответили верно на " + args.percentage + " вопросов<br>";
    final_content += "<div></div>";
    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;
    if (args.percentage >= 50){
        test_result = "пространственное";
    }
    else
        test_result = "no";
    send_result(test_result, test_number)
}


function results_test_10(args, test_number){
    let final_content = "";
    let test_result;
    final_content += "Вы ответили верно на " + args.percentage + " вопросов<br>";
    final_content += "<div></div>";
    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;
    if (args.percentage >= 50){
        test_result = "способности";
    }
    else
        test_result = "no";
    send_result(test_result, test_number)
}


function results_test_11(args, test_number){
    let final_content = "";
    let test_result;
    final_content += "Вы ответили верно на " + args.percentage + " вопросов<br>";
    final_content += "<div></div>";
    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;
     if (args.percentage >= 50){
        test_result = "внимательность";
    }
    else
        test_result = "no";
    send_result(test_result, test_number)
}


function results_test_12(args, test_number){
    let final_content = "";
    let test_result;
    final_content += "Вы ответили верно на " + args.percentage + " вопросов<br>";
    final_content += "<div></div>";
    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;
     if (args.percentage >= 50){
        test_result = "внимательность";
    }
    else
        test_result = "no";
    send_result(test_result, test_number)
}


function results_test_13(args, test_number){
    let final_content = "";
    let test_result;
    final_content += "Вы ответили верно на " + args.percentage + " вопросов<br>";
    final_content += "<div></div>";
    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;
     if (args.percentage >= 50){
        test_result = "способности";
    }
    else
        test_result = "no";
    send_result(test_result, test_number)
}


function results_test_14(args, test_number){
    let final_content = "";
    let _types_dict = {"nature": "человек природа" ,
               "technique": "человек техника",
               "signs": "человек знак",
               "creation": "человек художественный образ",
               "person": "человек человек"};
    let nature = "<div> человек - природа: " + args.nature + "</div>";
    let technique = "<div> человек - техника: " + args.technique + "</div>";
    let signs = "<div> человек - знак: " + args.signs + "</div>";
    let creation = "<div> человек - художественный образ: " + args.creation + "</div>";
    let person = "<div> человек- человек: " + args.person + "</div>";

    final_content += nature + technique + signs + creation + person;
    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;

    let _max = 0;
    let _type = "";
    for(let _key in args){
        if (parseInt(args[_key], 10) > _max){
            _max = parseInt(args[_key], 10);
            _type = _key;
        }
    }

    send_result(_types_dict.get(_type), test_number);
}


function results_test_15(args, test_number){
    let final_content = "";
    let labels_x = [];
    for(let i = 0; i < args.marks.length; i++)
    {
        labels_x[i] = i + 1;
    }

    new Chartist.Line('.ct-chart', {
      labels: labels_x,
      series: [args.marks]
    }, {
      fullWidth: true,
      chartPadding: {
        right: 40
      }
    });

    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;
    send_result("Done", test_number)
}


function results_test_16(args, test_number){
    let final_content = "";
    let points = args.points;
    let test_result;
    let result = "Качества лидера ";
    if (points <= 9) result += "выражены очень слабо";
    if ((points <= 24) && (points >= 10)) result += "выражены слабо";
    if ((points <= 34) && (points) >= 25) result += "выражены средне";
    if ((points <= 39) && (points) >= 35) result += "выражены сильно";
    if (points >= 40) result += "выражены очень сильно";

    final_content += result;
    let result_field = document.getElementById("result_field");
    result_field.innerHTML = final_content;
     if (args.points >= 50){
        test_result = "качества";
    }
    else
        test_result = "no";
    send_result(test_result, test_number)
}


function find_result_creator(test_number, args) {
    switch (test_number) {
        case 1:
            results_test_1(args, test_number);
            break;
        case 2:
            results_test_2(args, test_number);
            break;
        case 3:
            results_test_3(args, test_number);
            break;
        case 4:
            results_test_4(args, test_number);
            break;
        case 5:
            results_test_5(args, test_number);
            break;
        case 6:
            results_test_6(args, test_number);
            break;
        case 7:
            results_test_7(args, test_number);
            break;
        case 8:
            results_test_8(args, test_number);
            break;
        case 9:
            results_test_9(args, test_number);
            break;
        case 10:
            results_test_10(args, test_number);
            break;
        case 11:
            results_test_11(args, test_number);
            break;
        case 12:
            results_test_12(args, test_number);
            break;
        case 13:
            results_test_13(args, test_number);
            break;
        case 14:
            results_test_14(args, test_number);
            break;
        case 15:
            results_test_15(args, test_number);
            break;
        case 16:
            results_test_16(args, test_number);
            break;
        default:
            break;
    }
}