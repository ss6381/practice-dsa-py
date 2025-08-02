class FileStorageSystem:
    """
    Your task is the implement a simple cloud storage system that maps objects (files)
    to their metainformation. Specifically, the storage should maintain files and
    information about them (name, size, etc.). Note that this system should be in-memory:
    you don't need to work with the real filesystem.
    """

    def __init__(self):
        self.files = {}  # file_name -> {'size': int, 'owner': str}
        self.users = {}  # user_id -> {'capacity': int, 'used': int, 'files': set()}
        self.backups = {}  # user_id -> list of (name, size)

    # -------- Level 1 --------
    # The cloud storage system should support adding a new file and retrieving and deleting files.
    def add_file(self, name: str, size: int) -> bool:
        """
        Should add a new file name in the storage.
        size is the amount of memory required in bytes.
        The current operation fails if a file with the same name already exists.
        Return true if the file was added successfully or false otherwise.
        """
        if name in self.files:
            return False
        self.files[name] = {"size": size, "owner": "admin"}
        return True

    def get_file_size(self, name: str) -> int | None:
        """
        Returns the size of the file if it exists, or None otherwise.
        """
        if name in self.files:
            return self.files[name]["size"]
        return None

    def delete_file(self, name: str) -> int | None:
        """
        Deletes the file name, returns the deleted file's size if
        deletion was successful, or None otherwise if the file does not exist.
        """
        if name not in self.files:
            return None

        size = self.files[name]["size"]
        owner = self.files[name]["owner"]

        if owner != "admin":
            self.users[owner]["used"] -= size
            self.users[owner]["files"].remove(name)

        del self.files[name]
        return size

    # -------- Level 2 --------
    # The cloud storage system should support displaying the largest files.
    def get_n_largest(self, prefix: str, n: int) -> list[str]:
        """
        Should return the list of strings representing the names of the top
        n largest files with names starting with prefix in the following format:
        ["<name_1><size_1>", ... , "<name_n><size_n>"].
        Returned files should be sorted by size in descending order, or in case of a tie,
        sorted in lexicographical order of the names.
        If there are no such files, return an empty list.
        If the number of such files is less than n, all of them should be
        returned in the specified format.
        """
        filtered = [
            (name, file["size"])
            for name, file in self.files.items()
            if name.startswith(prefix)
        ]
        filtered.sort(key=lambda x: (-x[1], x[0]))
        return [f"{name}{size}" for name, size in filtered[:n]]

    # -------- Level 3 --------
    # The cloud storage system should support adding users with limited capacities and merging two users.
    def add_user(self, user_id: str, capacity: int) -> bool:
        """
        Add a new user to the system with capacity as their storage limit in bytes.
        Total size of all files owned by user_id cannot exceed capacity.
        """
        if user_id in self.users or user_id == "admin":
            return False
        self.users[user_id] = {"capacity": capacity, "used": 0, "files": set()}
        return True

    def add_file_by(self, user_id: str, name: str, size: int) -> int | None:
        """
        Same as add_file from Level 1, but added files should be owned by the user with user_id.
        New file cannot be added if doing so will exceed the user's capacity.
        Return the remaining capacity of the user if the file is successfully added, or None otherwise.
        """
        if name in self.files or user_id not in self.users:
            return None

        user = self.users[user_id]
        if user["used"] + size > user["capacity"]:
            return None

        self.files[name] = {"size": size, "owner": user_id}
        user["used"] += size
        user["files"].add(name)

        return user["capacity"] - user["used"]

    def merge_user(self, user_id_1: str, user_id_2: str) -> int | None:
        """
        Ownership of all of user_id_2's files is transferred to user_id_1, and
        any remaining storage capacity is also added to user_id_1's limit.
        user_id_2 is deleted if the merge is successful.
        Returns the remaining capacity of user_id_1 after merging, or None if
        one of the users does not exist or user_id_1 is equal to user_id_2.
        It is guaranteed that neither user_id_1 and user_id_2 equals "admin",
        who has unlimited storage capacity.
        """
        if user_id_1 == user_id_2:
            return None
        if user_id_1 not in self.users or user_id_2 not in self.users:
            return None

        user1 = self.users[user_id_1]
        user2 = self.users[user_id_2]

        for fname in list(user2["files"]):
            self.files[fname]["owner"] = user_id_1
            user1["files"].add(fname)

        user1["capacity"] += user2["capacity"]
        user1["used"] += user2["used"]
        del self.users[user_id_2]

        return user1["capacity"] - user1["used"]

    # -------- Level 4 --------
    # The cloud storage system should support backing up and restoring a user's files.
    def backup(self, user_id: str) -> bool:
        if user_id not in self.users:
            return False
        self.backups[user_id] = []
        for fname in self.users[user_id]["files"]:
            size = self.files[fname]["size"]
            self.backups[user_id].append((fname, size))
        return True

    def restore(self, user_id: str) -> bool:
        if user_id not in self.users or user_id not in self.backups:
            return False

        backup_files = self.backups[user_id]
        current_files = self.users[user_id]["files"]

        # Check if any backup files exist (collide with other users or admin)
        for name, _ in backup_files:
            if name in self.files and self.files[name]["owner"] != user_id:
                return False  # collision

        # Step 1: delete current user's files
        for fname in list(current_files):
            self.delete_file(fname)

        # Step 2: re-add files from backup
        user = self.users[user_id]
        for name, size in backup_files:
            self.files[name] = {"size": size, "owner": user_id}
            user["files"].add(name)
            user["used"] += size

        return True
