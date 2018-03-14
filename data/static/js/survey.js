Survey.StylesManager.applyTheme("default");

var json = {
    title: "Итак, познакомимся!",
    triggers: [
        {
            type: "complete",
            name: "has_money",
            operator: "notequal",
            value: "Да, много"
        }
    ], pages: [
        {
			questions: [
				{
					name: "name",
					type: "text",
					title: "Привет! Как тебя зовут?",
					placeHolder: "Вовочка Пупкин",
					isRequired: true
				}
			]
        }, {
            questions: [
                {
					type: "radiogroup",
					name: "has_money",
					title: "Отлично, {name}! Ты в двух шагах от успеха! У тебя есть деньги?",
					isRequired: true,
					choices: [
						"Да, много",
						"Нет, и никогда не было",
						"Были, но все потратил"
					]
				}
            ]
        }, {
            questions: [
                {
					type: "radiogroup",
					name: "is_generous",
					title: "{name}, друг, скажи честно: ты со мной поделишься?",
					isRequired: true,
					choices: [
						"Да, конечно",
						"С чего бы вдруг???"
					]
				}
            ]
        }
    ],
	completedHtml: "Хм..."
};

window.survey = new Survey.Model(json);

survey.onComplete.add(function (result) {
	var has_money = (result.data.has_money == "Да, много");
	var is_generous = (result.data.is_generous == "Да, конечно");
	var answer = [
		'И чего ты тут расселся??? Иди работай!',
		'Ну, ты и жадина! Иди и хорошенько подумай над своим поведением.',
		'Отлично! Следуй за белым кроликом (admin/survey11)...'
	];
	var res = !has_money ? 0 : !is_generous ? 1 : 2;

	$.ajax({
		type: 'POST',
		contentType: 'application/json',
		url: '/api/survey/',
		data: JSON.stringify({ 'name': result.data.name, 'has_money': has_money, 'is_generous': is_generous})
	});

	document.querySelector('#surveyResult').innerHTML = answer[res];
	if (res==2) {
		$('#rabbit').addClass('blue-bgr');
	}
});

$("#surveyElement").Survey({model: survey});