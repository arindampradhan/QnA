const Model = {
    username: '',
    total_user: 0,
    total_questions: 0,
    questions: [],
    user_id: ''
}

function call_initalization() {
    $.ajax({
        url: "/api/questions",
        headers: {"api_key": store.get('user')['api_key']}
    }).then((response) => {store.set('questions', response);updateDom() })

    $.ajax({
        url: "/api/count",
        headers: {"api_key": store.get('user')['api_key']}
    }).then((response) => { store.set('count', response);updateDom() })

    $.ajax({
        url: "/getuser",
        headers: {"api_key": store.get('user')['api_key']}
    }).then((response) => { store.set('user', response);updateDom() })

    $.ajax({
        url: "/api/questions",
        headers: {"api_key": store.get('user')['api_key']}
    }).then((response)=>{store.set('questions', response);updateQnA()})
}

function fetch_answer(question_id) {
    $.get(`/api/answer/${question_id}`)
        .then((response) => { store.set(`question_${question_id}`, response.data);updateDom() })
}

// update dom
function updateDom() {
    // cards
    var q = store.get('count')['question_count']
    var u = store.get('count')['user_count']
    $("#user_count").html(u)
    $("#total_questions").html(q)

    // header
    $('#user_name').html(store.get('user')['username'])
    $('#rate_limit').html(store.get('user')['request_count'])
    $("#api_key").val(store.get('user')['api_key'])
}


function updateQnA() {

    function render(obj, index) {
        let answers = "";
        obj.answers.forEach((item)=> {
            const temp = `
                <blockquote>
                 <p class="larger">
                    ${item.body || 'New Delhi'}
                 </p>
                 <small>
                    <b>id</b>: ${item['_id']['$oid'] || 'asddsadasasdsaddsaqw12321321sdasd'}
                 </small>
                </blockquote>            
            `
            answers += temp;
        })
        const panel = `
            <div class="panel panel-border">
                <div class="panel-heading accordion-toggle question-toggle collapsed" data-toggle="collapse" data-parent="#faqAccordion" data-target="${'#question' + index}">
                     <h4 class="panel-title">
                        <a href="#" class="ing">Q: <span id="question_title">${obj.title || 'What is the capital of india?'} </span></a>
                        &nbsp;&nbsp;&nbsp; ${obj.private ? '<span class="badge">private</span>':''}
                  </h4>
            
                </div>
                <div id="${'question' + index}" class="panel-collapse collapse" style="height: 0px;">
                    <div class="panel-body">
                        ${answers}
                    </div>
                </div>
            </div>
        `;
        return panel
    }

    $('#faqAccordion').html('')
    const questions = store.get('questions')
    questions.forEach((item,index)=> {
        let panelItem = render(item, index);
        $('#faqAccordion').append(panelItem)
    })

}

// initial point
$.get('/getuser')
    .then((response) =>{ store.set('user', response); call_initalization() })
