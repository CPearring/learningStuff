dpkg -s auditd | grep Status
apt-get install -y auditd
dpkg -s auditd | grep Status
inspec help
inspec detect
cd /root
git clone https://github.com/learn-chef/auditd.git
tree auditd
cat auditd/controls/example.rb 
inspec exec /root/auditd/
inspec exec auditd -t ssh://root:password@target
inspec exec auditd -t ssh://root:password@target --reporter=json | jq .
inspec check auditd
inspec archive auditd
ls | grep auditd
exit
