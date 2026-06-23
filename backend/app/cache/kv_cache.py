class KVCache:

    def __init__(self):

        self.sessions = {}

    def store(
        self,
        session_id,
        key,
        value
    ):

        if session_id not in self.sessions:

            self.sessions[
                session_id
            ] = {}

        self.sessions[
            session_id
        ][key] = value

    def get(
        self,
        session_id,
        key
    ):

        return (
            self.sessions
            .get(
                session_id,
                {}
            )
            .get(
                key
            )
        )

    def get_session(
        self,
        session_id
    ):

        return self.sessions.get(
            session_id,
            {}
        )

    def delete_session(
        self,
        session_id
    ):

        self.sessions.pop(
            session_id,
            None
        )