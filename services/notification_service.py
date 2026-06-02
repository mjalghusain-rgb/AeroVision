from data.notifications import NOTIFICATIONS


class NotificationService:

    def __init__(self):

        self.notifications = NOTIFICATIONS

    def get_all_notifications(self):

        return self.notifications

    def get_notification_by_id(
        self,
        notification_id
    ):

        notification_id = (
            notification_id.upper()
        )

        for notification in self.notifications:

            if (
                notification["notification_id"]
                == notification_id
            ):

                return notification

        return None

    def search(
        self,
        query
    ):

        query = query.lower()

        results = []

        for notification in self.notifications:

            if (

                query in notification["notification_id"].lower()

                or

                query in notification["title"].lower()

                or

                query in notification["message"].lower()

                or

                query in notification["type"].lower()

                or

                query in notification["status"].lower()

            ):

                results.append(
                    notification
                )

        return results

    def get_by_type(
        self,
        notification_type
    ):

        notification_type = (
            notification_type.lower()
        )

        results = []

        for notification in self.notifications:

            if (
                notification["type"].lower()
                == notification_type
            ):

                results.append(
                    notification
                )

        return results

    def get_by_status(
        self,
        status
    ):

        status = (
            status.lower()
        )

        results = []

        for notification in self.notifications:

            if (
                notification["status"].lower()
                == status
            ):

                results.append(
                    notification
                )

        return results

    def total_notifications(self):

        return len(
            self.notifications
        )

    def unread_notifications(self):

        return len(
            self.get_by_status(
                "Unread"
            )
        )

    def read_notifications(self):

        return len(
            self.get_by_status(
                "Read"
            )
        )
