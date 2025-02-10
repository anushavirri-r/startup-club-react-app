export default class APIService {
    static LoginUser(body) {

        return fetch('/choreo-apis/djangoreactsuclub/backend/v1/auth/', {
            'method': 'POST',
            headers: {
                'Content-Type': 'application/json',

            },
            body: JSON.stringify(body)

        }).then(resp => resp.json())

    }


    static RegisterUser(body) {

        return fetch('/choreo-apis/djangoreactsuclub/backend/v1/Frontend/users/', {
            'method': 'POST',
            headers: {
                'Content-Type': 'application/json',

            },
            body: JSON.stringify(body)

        }).then(resp => resp.json())

    }

}