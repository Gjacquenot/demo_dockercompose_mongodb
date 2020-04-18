db.auth('admin-user', 'admin-password')

db.createUser({
  user: 'test-user',
  pwd: 'test-password',
  roles: [
    {
      role: 'readWrite',
      db: 'test-database',
    },
  ],
});
