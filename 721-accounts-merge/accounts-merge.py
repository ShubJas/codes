class Solution:
    def find(self, x):
        # Path compression heuristic to find the root of x
        # If x is not its own parent, recursively find the root and update the parent of x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        # Find the roots of the sets u and v belong to
        root_u = self.find(u)
        root_v = self.find(v)

        # If the roots are the same, u and v are already connected
        if root_u == root_v:
            return False

        # Union by rank: attach the smaller tree under the root of the deeper tree
        if self.rank[root_u] < self.rank[root_v]:
            root_u, root_v = root_v, root_u

        # Update the parent of root_v to root_u
        self.parent[root_v] = root_u

        # Update the rank if necessary
        if self.rank[root_u] == self.rank[root_v]:
            self.rank[root_u] += 1

        return True

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        encoding = {}  # Dictionary to map emails to unique IDs
        emails = set()  # Set to collect all unique emails
        
        # Collect all unique emails and assign a unique ID to each
        for acc in accounts:
            for email in acc[1:]:
                emails.add(email)
        
        n = len(emails)  # Total number of unique emails
        self.parent = list(range(n))  # Initialize parent list where each email is its own parent
        self.rank = [1] * n  # Initialize rank list with each email having rank 1
        email_to_id = {email: idx for idx, email in enumerate(emails)}  # Map each email to a unique ID

        # Union emails in the same account to the same set
        for acc in accounts:
            first_email_id = email_to_id[acc[1]]  # Get the ID of the first email in the account
            for email in acc[2:]:
                self.union(first_email_id, email_to_id[email])  # Union this email with all other emails in the account

        # Collect emails by their root parent to group connected components
        id_to_emails = defaultdict(list)
        for email in emails:
            root_id = self.find(email_to_id[email])  # Find the root ID of the email
            id_to_emails[root_id].append(email)  # Append the email to the list of its root parent

        # Prepare the merged account list
        merged_accounts = []
        for acc in accounts:
            name = acc[0]  # Get the name of the account holder
            root_id = self.find(email_to_id[acc[1]])  # Get the root ID of the first email in the account
            if root_id in id_to_emails:
                merged_accounts.append([name] + sorted(id_to_emails.pop(root_id)))  # Append the merged account to the result list

        return merged_accounts
