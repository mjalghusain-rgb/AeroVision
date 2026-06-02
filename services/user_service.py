from data.users import USERS


class UserService:

    def __init__(self):

        self.users = USERS

    def get_all_users(self):

        return self.users

    def get_user_by_id(
        self,
        user_id
    ):

        user_id = (
            user_id.upper()
        )

        for user in self.users:

            if (
                user["user_id"]
                == user_id
            ):

                return user

        return None

    def get_user_by_username(
        self,
        username
    ):

        username = (
            username.lower()
        )

        for user in self.users:

            if (
                user["username"].lower()
                == username
            ):

                return user

        return None

    def search(
        self,
        query
    ):

        query = query.lower()

        results = []

        for user in self.users:

            if (

                query in user["user_id"].lower()

                or

                query in user["username"].lower()

                or

                query in user["email"].lower()

                or

                query in user["role"].lower()

                or

                query in user["language"].lower()

                or

                query in user["status"].lower()

            ):

                results.append(
                    user
                )

        return results

    def get_by_role(
        self,
        role
    ):

        role = role.lower()

        results = []

        for user in self.users:

            if (
                user["role"].lower()
                == role
            ):

                results.append(
                    user
                )

        return results

    def get_by_status(
        self,
        status
    ):

        status = status.lower()

        results = []

        for user in self.users:

            if (
                user["status"].lower()
                == status
            ):

                results.append(
                    user
                )

        return results

    def total_users(self):

        return len(
            self.users
        )

    def total_admins(self):

        return len(
            self.get_by_role(
                "Admin"
            )
        )

    def total_active_users(self):

        return len(
            self.get_by_status(
                "Active"
            )
        )
