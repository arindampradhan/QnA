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
    }).then((response)=>{store.set('questions', response)})
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

// initial point
$.get('/getuser')
    .then((response) =>{ store.set('user', response);call_initalization()})
