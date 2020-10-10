# use the official wordpress Docker image
FROM wordpress

# install curl and jq
RUN apt update && apt install -y jq curl

# install latest release of woocommerce from github
RUN mkdir /usr/src/wordpress/wp-content/plugins/woocommerce \
  && curl -sL $(curl -sL -H "Accept: application/vnd.github.v3.full+json" \
  https://api.github.com/repos/woocommerce/woocommerce/releases/latest \
  | jq -r .tarball_url) \
  | tar zx -C /usr/src/wordpress/wp-content/plugins/woocommerce \--strip-components 1

# install latest release of gutenberg
RUN mkdir /usr/src/wordpress/wp-content/plugins/gutenberg \
  && curl -sL $(curl -sL -H "Accept: application/vnd.github.v3.full+json" \
  https://api.github.com/repos/WordPress/gutenberg/releases/latest \
  | jq -r .tarball_url) \
  | tar zx -C /usr/src/wordpress/wp-content/plugins/gutenberg \--strip-components 1

# install latest release of wordfence
RUN mkdir /usr/src/wordpress/wp-content/plugins/wordfence \
  && curl -sL -H "Accept: application/vnd.github.v3.full+json" \
  https://api.github.com/repos/wp-plugins/wordfence/tarball/master \
  | tar zx -C /usr/src/wordpress/wp-content/plugins/wordfence \--strip-components 1