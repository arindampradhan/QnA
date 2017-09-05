const Model = {
    username: '',
    total_user: 0,
    total_questions: 0,
    questions: [],
    user_id: ''
}

function call_initalization() {
    $.get('/api/questions')
        .then((response) => store.set('questions', response))

    $.get('/api/count')
        .then((response) => store.set('count', response))

    $.get('/getuser')
        .then((response) => store.set('user', response.user))
}

function fetch_answer(question_id) {
    $.get(`/api/answer/${question_id}`)
        .then((response) => store.set(`question_${question_id}`, response.data))
}

call_initalization()

// update dom
store.watch('count', function() {
    var q = this.get('count')['question_count']
    var u = this.get('count')['user_count']
    $("#user_count").html(u)
    $("#total_questions").html(q)
    Model.total_user = u
    Model.total_questions = q
})

store.watch('user', function() {
    $('#user_name').html(this.get('user'))
    Modal.username = this.get('user')
})
