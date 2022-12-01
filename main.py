from flask import Flask
# import datetime

# app = Flask(__name__)
app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Primary Meta Tags -->
    <title>
      Lancolatech Company Limited - Dental management system, Bulk SMS, Digital
      marketing, Web design
    </title>
    <meta
      name="title"
      content="Lancolatech Company - Bulk SMS, Dental management system"
    />
    <meta
      name="description"
      content="A limited company with a mission of providing IT solutions to all our clients irrespective of
their sizes.
"
    />

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://metatags.io/" />
    <meta
      property="og:title"
      content="Lancolatech Company - Bulk SMS, Dental management system, Digital marketing, Web design"
    />
    <meta
      property="og:description"
      content="A limited company with a mission of providing IT solutions to all our clients irrespective of
their sizes.
"
    />
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="https://metatags.io/" />
    <meta
      property="twitter:title"
      content="Lancolatech Company - Bulk SMS, Dental management system, Digital marketing, Web design"
    />
    <meta
      property="twitter:description"
      content="A limited company with a mission of providing IT solutions to all our clients irrespective of
their sizes.
"
    />

    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
  </head>

  <body>
    <div class="main-wrapper">
      <!-- Preloader start -->
      <!-- <div id="preloader">
            <div class="preloader">
                <span></span>
                <span></span>
            </div>
        </div> -->
      <!-- Preloader End -->

      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.webp"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li class="active-menu">
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li>
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <!-- Header Search Start -->
              <!-- Header Search End -->

              <!-- Header Cart Start -->

              <!-- Header Cart End -->
              <!-- Header Info Start -->
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a
                  class="btn"
                  href="mailto:info@lancolatech.co.ke"
                  target="_blank"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling & Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li><a href="data-analytics">Data Analytics</a></li>
                  <li><a href="graphics-design">graphics Design</a></li>
                </ul>
              </li>
              <li><a href="pricing">Pricing</a></li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
                <!-- <li><a href="https://blog.lancolatech.co.ke" target="_blank">Gallery</a> -->
              </li>

              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <!-- Hero Start -->
      <!-- <div class="section tech-hero-section-2 d-flex align-items-center" style="background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/hero-2.webp);">
            <div class="shape-1"></div>
            <div class="shape-2"></div>
            <div class="shape-3"></div>
            <div class="shape-4"></div>
            <div class="shape-5"></div>
            <div class="container">
                <div class="row">
                    <div class="col-xl-6">
                        <div class="hero-content">
                            <h3 class="sub-title" data-aos-delay="600" data-aos="fade-up">Unlocking Potential & Oppotunities</h3>
                            <h2 class="title" data-aos="fade-up" data-aos-delay="800">A Company focused on top technology</h2>
                            <div class="hero-btn" data-aos="fade-up" data-aos-delay="1000">
                                <a class="btn" href="/about">Read More</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div> -->
      <div
        class="section tech-hero-section"
        style="
          background-image: url(https://res.cloudinary.com/weknow-creators/image/upload/v1665668919/lancola/LANC_SLIDER_ekh5wt.webp);
        "
      >
        <!-- <div class="shape-1"></div> -->
        <div class="container">
          <div class="row">
            <div class="col-xl-6">
              <!-- Hero Content Start -->
              <div class="hero-content">
                <h3 class="sub-title" data-aos-delay="600" data-aos="fade-up">
                  Technology Related Consultancy
                </h3>
                <h2 class="title" data-aos="fade-up" data-aos-delay="700">
                  We bring great Ideas to life
                </h2>
                <!-- <p data-aos="fade-up" data-aos-delay="800">We provide the most responsive and functional IT design for companies and businesses worldwide.</p> -->
                <div class="hero-btn" data-aos="fade-up" data-aos-delay="900">
                  <a class="btn" href="/about">Read More</a>
                </div>
              </div>
              <!-- Hero Content End -->
            </div>
          </div>
        </div>
      </div>
      <!-- Hero End -->

      <!-- Service-2 Start -->
      <div
        class="section features-section-3 features-section-4 features-section-6 section-padding"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg//features-6-bg.jpg);
        "
      >
        <div class="container">
          <!-- Features Wrap Start -->
          <div class="features-wrap-3">
            <div class="row">
              <div class="col-lg-8">
                <div class="section-title2">
                  <h2 class="title">
                    We run all kinds of <span>IT services</span> that vow your
                    success
                  </h2>
                </div>
              </div>
              <div class="col-lg-4">
                <!-- <div class="features-6-btn">
                                <a class="btn" href="/service">All Services</a>
                            </div> -->
              </div>
            </div>
            <div class="features-content-wrap">
              <div class="row">
                <div class="col-lg-4 col-sm-6">
                  <!-- Single Item Start -->
                  <div class="single-item">
                    <div class="features-icon">
                      <img
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/sms.png"
                        alt=""
                      />
                    </div>
                    <div class="features-content">
                      <h3 class="title">Bulk SMS</h3>
                      <p>
                        We provide customized bulk SMS, SMS gateway, free SMS
                        API, free SMS software and bulk data bundles to our
                        customers at the most affordable rates.
                      </p>
                    </div>
                  </div>
                  <!-- Single Item End -->
                </div>
                <div class="col-lg-4 col-sm-6">
                  <!-- Single Item Start -->
                  <div class="single-item">
                    <div class="features-icon">
                      <img
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/mntsys.png"
                        alt=""
                      />
                    </div>
                    <div class="features-content">
                      <h3 class="title">Management Systems</h3>
                      <p>
                        With our Management System, we provide you with
                        easy-to-use tools for all your work structures.
                      </p>
                    </div>
                  </div>
                  <!-- Single Item End -->
                </div>
                <div class="col-lg-4 col-sm-6">
                  <!-- Single Item Start -->
                  <div class="single-item">
                    <div class="features-icon">
                      <img
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/download.png"
                        alt=""
                      />
                    </div>
                    <div class="features-content">
                      <h3 class="title">Digital marketing</h3>
                      <p>
                        Our team of social media experts will help you increase
                        your visibility on popular networks such as Facebook,
                        Twitter and Instagram.
                      </p>
                    </div>
                  </div>
                  <!-- Single Item End -->
                </div>
                <div class="col-lg-4 col-sm-6">
                  <!-- Single Item Start -->
                  <div class="single-item">
                    <div class="features-icon">
                      <img
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/solution.png"
                        alt=""
                      />
                    </div>
                    <div class="features-content">
                      <h3 class="title">Computer solutions</h3>
                      <p>
                        We offer network cables, systems, and solutions that
                        meet the highest industry specifications; form factors
                        that fit their customers' requirements.
                      </p>
                    </div>
                  </div>
                  <!-- Single Item End -->
                </div>
                <div class="col-lg-4 col-sm-6">
                  <!-- Single Item Start -->
                  <div class="single-item">
                    <div class="features-icon">
                      <img
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/access.png"
                        alt=""
                      />
                    </div>
                    <div class="features-content">
                      <h3 class="title">Computer accessories</h3>
                      <p>
                        We strive to ensure our customers know exactly what they
                        are buying, with the best prices and product quality
                        from the trusted Computer Accessories suppliers.
                      </p>
                    </div>
                  </div>
                  <!-- Single Item End -->
                </div>
                <div class="col-lg-4 col-sm-6">
                  <!-- Single Item Start -->
                  <div class="single-item">
                    <div class="features-icon">
                      <img
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/cctv.png"
                        alt=""
                      />
                    </div>
                    <div class="features-content">
                      <h3 class="title">CCTV Installtions</h3>
                      <p>
                        We specialize in home and business security systems.
                        From a simple home network to CCTV cameras, we service
                        all types of installations.
                      </p>
                    </div>
                  </div>
                  <!-- Single Item End -->
                </div>
              </div>
            </div>
          </div>
          <!-- Features Wrap End -->
        </div>
      </div>
      <!-- Features End -->

      <!-- Team Start -->
      <div class="section team-section section-padding">
        <div class="container">
          <!-- Team Wrap Start -->
          <div class="team-wrap">
            <div class="section-title text-center">
              <h3 class="sub-title">Our Highly Professional Staffs</h3>
              <h2 class="title">
                IT technology and technical fields professional staff
              </h2>
            </div>
            <!-- Team Content Wrap Start -->
            <div class="team-content-wrap">
              <div class="row">
                <div class="col-xl-3 col-lg-4 col-md-6">
                  <!-- Single Team Start -->
                  <div class="single-team">
                    <div class="team-img">
                      <a href="#"
                        ><img
                          src="https://res.cloudinary.com/weknow-creators/image/upload/v1665741385/lancola/IMG_allan_qprcrq.avif"
                          alt="allan"
                      /></a>
                    </div>
                    <div class="team-content">
                      <div class="team-social">
                        <ul class="social">
                          <li>
                            <a href="https://twitter.com"
                              ><i class="fab fa-twitter"></i
                            ></a>
                          </li>
                          <li>
                            <a href="https://github.com"
                              ><i class="fab fa-github"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                      <h3 class="name"><a href="#">Allan Rop</a></h3>
                      <span class="designation">Founder | CEO</span>
                    </div>
                  </div>
                  <!-- Single Team End -->
                </div>
                <div class="col-xl-3 col-lg-4 col-md-6">
                  <!-- Single Team Start -->
                  <div class="single-team">
                    <div class="team-img">
                      <a href="#"
                        ><img
                          src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/team/team-6.jpg"
                          alt="martin"
                      /></a>
                    </div>
                    <div class="team-content">
                      <div class="team-social">
                        <ul class="social">
                          <li>
                            <a href="https://twitter.com"
                              ><i class="fab fa-twitter"></i
                            ></a>
                          </li>
                          <li>
                            <a href="https://github.com"
                              ><i class="fab fa-github"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                      <h3 class="name"><a href="#">Martin Tarus</a></h3>
                      <span class="designation">Director</span>
                    </div>
                  </div>
                  <!-- Single Team End -->
                </div>
                <div class="col-xl-3 col-lg-4 col-md-6">
                  <!-- Single Team Start -->
                  <div class="single-team">
                    <div class="team-img">
                      <a href="#"
                        ><img
                          src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/IMG_5452.jpg"
                          alt="Alfred"
                      /></a>
                    </div>
                    <div class="team-content">
                      <div class="team-social">
                        <ul class="social">
                          <li>
                            <a href="https://twitter.com"
                              ><i class="fab fa-twitter"></i
                            ></a>
                          </li>
                          <li>
                            <a href="https://github.com"
                              ><i class="fab fa-github"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                      <h3 class="name"><a href="#">Alfred Okaka</a></h3>
                      <span class="designation">Director</span>
                    </div>
                  </div>
                  <!-- Single Team End -->
                </div>
                <div class="col-xl-3 col-lg-4 col-md-6">
                  <!-- Single Team Start -->
                  <div class="single-team">
                    <div class="team-img">
                      <a href="#"
                        ><img
                          src="https://res.cloudinary.com/weknow-creators/image/upload/v1664187407/lancola/vin_1_qscva71_1_j1wd5p.avif"
                          alt="vincent"
                      /></a>
                    </div>
                    <div class="team-content">
                      <div class="team-social">
                        <ul class="social">
                          <li>
                            <a href="https://twitter.com"
                              ><i class="fab fa-twitter"></i
                            ></a>
                          </li>
                          <li>
                            <a href="https://github.com"
                              ><i class="fab fa-github"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                      <h3 class="name"><a href="#">Vincent Tulus</a></h3>
                      <span class="designation">Support | Web Developer</span>
                    </div>
                  </div>
                  <!-- Single Team End -->
                </div>
                <div class="col-xl-3 col-lg-4 col-md-6">
                  <!-- Single Team Start -->
                  <div class="single-team">
                    <div class="team-img">
                      <a href="#"
                        ><img
                          src="https://res.cloudinary.com/weknow-creators/image/upload/v1665741384/lancola/IMG_derrick_vsxvo3.avif"
                          alt="Derrick"
                      /></a>
                    </div>
                    <div class="team-content">
                      <div class="team-social">
                        <ul class="social">
                          <li>
                            <a href="https://twitter.com"
                              ><i class="fab fa-twitter"></i
                            ></a>
                          </li>
                          <li>
                            <a href="https://github.com"
                              ><i class="fab fa-github"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                      <h3 class="name"><a href="#">Derrick Otieno</a></h3>
                      <span class="designation">CCTV Technician</span>
                    </div>
                  </div>
                  <!-- Single Team End -->
                </div>
                <!-- <div class="col-xl-3 col-lg-4 col-md-6"> -->
                <!-- Single Team Start -->
                <!-- <div class="single-team">
                    <div class="team-img">
                      <a href="#"
                        ><img
                          src="https://res.cloudinary.com/weknow-creators/image/upload/v1665486825/lancola/IMG_5065lynne_ppqy3b.avif"
                          alt="Lynne"
                      /></a>
                    </div>
                    <div class="team-content">
                      <div class="team-social">
                        <ul class="social">
                          <li>
                            <a href="https://twitter.com"
                              ><i class="fab fa-twitter"></i
                            ></a>
                          </li>
                          <li>
                            <a href="https://github.com"
                              ><i class="fab fa-github"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                      <h3 class="name"><a href="#">Lynne Chebii</a></h3>
                      <span class="designation">Accountant</span>
                    </div>
                  </div> -->
                <!-- Single Team End -->
                <!-- </div> -->
                <div class="col-xl-3 col-lg-4 col-md-6">
                  <!-- Single Team Start -->
                  <div class="single-team">
                    <div class="team-img">
                      <a href="#"
                        ><img
                          src="https://res.cloudinary.com/weknow-creators/image/upload/v1664187403/lancola/mike_eiueup1_1_cxxde4.avif"
                          alt="Mike"
                      /></a>
                    </div>
                    <div class="team-content">
                      <div class="team-social">
                        <ul class="social">
                          <li>
                            <a href="https://twitter.com"
                              ><i class="fab fa-twitter"></i
                            ></a>
                          </li>
                          <li>
                            <a href="https://github.com"
                              ><i class="fab fa-github"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                      <h3 class="name"><a href="#">Mike Owino</a></h3>
                      <span class="designation">Support | Web Developer</span>
                    </div>
                  </div>

                  <!-- Single Team End -->
                </div>

                <div class="col-xl-3 col-lg-4 col-md-6">
                  <div class="single-team">
                    <div class="team-img">
                      <a href="#"
                        ><img
                          src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/team/team-6.jpg"
                          alt="Julius"
                      /></a>
                    </div>
                    <div class="team-content">
                      <div class="team-social">
                        <ul class="social">
                          <li>
                            <a href="https://twitter.com"
                              ><i class="fab fa-twitter"></i
                            ></a>
                          </li>
                          <li>
                            <a href="https://github.com"
                              ><i class="fab fa-github"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                      <h3 class="name"><a href="#">Julius Kimutai</a></h3>
                      <span class="designation">Support</span>
                    </div>
                  </div>
                </div>
                <div class="col-xl-3 col-lg-4 col-md-6">
                  <div class="single-team">
                    <div class="team-img">
                      <a href="#"
                        ><img
                          src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/team/team-6.jpg"
                          alt="Julius"
                      /></a>
                    </div>
                    <div class="team-content">
                      <div class="team-social">
                        <ul class="social">
                          <li>
                            <a href="https://twitter.com"
                              ><i class="fab fa-twitter"></i
                            ></a>
                          </li>
                          <li>
                            <a href="https://github.com"
                              ><i class="fab fa-github"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                      <h3 class="name"><span>Daisy Chebet</span></h3>
                      <span class="designation">Accountant</span>
                    </div>
                  </div>
                </div>
                <div class="col-xl-3 col-lg-4 col-md-6">
                  <!-- Single Team Start -->
                  <div class="single-team">
                    <div class="team-img">
                      <a href="#"
                        ><img
                          src="https://res.cloudinary.com/weknow-creators/image/upload/v1664187405/lancola/G1_f7s13f1_1_rmztcg.avif"
                          alt="Grevians"
                      /></a>
                    </div>
                    <div class="team-content">
                      <div class="team-social">
                        <ul class="social">
                          <li>
                            <a href="https://twitter.com"
                              ><i class="fab fa-twitter"></i
                            ></a>
                          </li>
                          <li>
                            <a href="https://github.com"
                              ><i class="fab fa-github"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                      <h3 class="name"><a href="#">Grevians Onula</a></h3>
                      <span class="designation">Digital Marketer</span>
                    </div>
                  </div>
                  <!-- Single Team End -->
                </div>
                <div class="col-xl-3 col-lg-4 col-md-6">
                  <!-- Single Team Start -->
                  <div class="single-team">
                    <div class="team-img">
                      <a href="#"
                        ><img
                          src="https://res.cloudinary.com/weknow-creators/image/upload/v1665486980/lancola/IMG_4941-Editvic_qhcq8b.avif"
                          alt="Victoria"
                      /></a>
                    </div>
                    <div class="team-content">
                      <div class="team-social">
                        <ul class="social">
                          <li>
                            <a href="https://twitter.com"
                              ><i class="fab fa-twitter"></i
                            ></a>
                          </li>
                          <li>
                            <a href="https://github.com"
                              ><i class="fab fa-github"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                      <h3 class="name"><a href="#">Victoria Cherotich</a></h3>
                      <span class="designation">Software Developer</span>
                    </div>
                  </div>
                  <!-- Single Team End -->
                </div>
              </div>
            </div>
            <!-- Team Content Wrap End -->
          </div>
          <!-- Team Wrap End -->
        </div>
      </div>
      <!-- Team End -->

      <!-- Testimonial Start -->
      <div
        class="section testimonial-section section-padding"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/testi-bg.jpg);
        "
      >
        <div class="container">
          <!-- Testimonial Wrap Start -->
          <div class="testimonial-wrap">
            <div class="row">
              <div class="col-xl-4">
                <div class="section-title">
                  <h3 class="sub-title">Client Testimonial</h3>
                  <h2 class="title">
                    100+ clients love our service & IT related solutions
                  </h2>
                </div>
              </div>
              <div class="col-xl-8">
                <!-- Testimonial Slider Wrap Start -->
                <div class="testimonial-slider-wrap">
                  <div class="swiper-container testimonial-active">
                    <div class="swiper-wrapper">
                      <div class="swiper-slide">
                        <!-- Single Testimonial Start -->
                        <div class="single-testimonial">
                          <div class="testimonial-content">
                            <h3 class="title">They Are Best</h3>
                            <p>
                              The amount of good causes you promote and the
                              resources you share with everyone is nothing short
                              of inspirational. Your commitment to helping us
                              all grow shows how caring and thoughtful you are,
                              which shines through in everything you do!
                            </p>
                            <div class="testimonial-author-wrap">
                              <div class="testimonial-author">
                                <!-- <div class="author-img">
                                                                <img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/author-1.jpg" alt="">
                                                            </div> -->
                                <div class="author-text">
                                  <h5 class="name">Dentatouch Clinic</h5>
                                  <span class="designation">Eldoret</span>
                                </div>
                              </div>
                              <div class="testimonial-quote">
                                <img
                                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/quote.png"
                                  alt=""
                                />
                              </div>
                            </div>
                          </div>
                        </div>
                        <!-- Single Testimonial End -->
                      </div>
                      <div class="swiper-slide">
                        <!-- Single Testimonial Start -->
                        <div class="single-testimonial">
                          <div class="testimonial-content">
                            <h3 class="title">Right Aagency</h3>
                            <p>
                              You have the natural ability to understand and
                              feel what your customers are experiencing, and you
                              are able to meet their needs effectively. Well
                              done!
                            </p>
                            <div class="testimonial-author-wrap">
                              <div class="testimonial-author">
                                <!--  <div class="author-img">
                                                                <img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/author-2.jpg" alt="">
                                                            </div> -->
                                <div class="author-text">
                                  <h5 class="name">Mike Wesa</h5>
                                  <span class="designation">Hala Clinic</span>
                                </div>
                              </div>
                              <div class="testimonial-quote">
                                <img
                                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/quote.png"
                                  alt=""
                                />
                              </div>
                            </div>
                          </div>
                        </div>
                        <!-- Single Testimonial End -->
                      </div>
                      <div class="swiper-slide">
                        <!-- Single Testimonial Start -->
                        <div class="single-testimonial">
                          <div class="testimonial-content">
                            <h3 class="title">Great job</h3>
                            <p>
                              You excel at serving your customers. Great job!
                            </p>
                            <div class="testimonial-author-wrap">
                              <div class="testimonial-author">
                                <!-- <div class="author-img">
                                                                <img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/author-1.jpg" alt="">
                                                            </div> -->
                                <div class="author-text">
                                  <h5 class="name">Dr.Statham</h5>
                                  <span class="designation"
                                    >Mwewe Hospital</span
                                  >
                                </div>
                              </div>
                              <div class="testimonial-quote">
                                <img
                                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/quote.png"
                                  alt=""
                                />
                              </div>
                            </div>
                          </div>
                        </div>
                        <!-- Single Testimonial End -->
                      </div>
                      <div class="swiper-slide">
                        <!-- Single Testimonial Start -->
                        <div class="single-testimonial">
                          <div class="testimonial-content">
                            <h3 class="title">Recommended</h3>
                            <p>
                              A fantastic organisation! Great cutomer support
                              from beginning to end of the process. The team are
                              really informed and go the extra mile at every
                              stage. I would recommend them unreservedly.
                            </p>
                            <div class="testimonial-author-wrap">
                              <div class="testimonial-author">
                                <!-- <div class="author-img">
                                                                <img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/author-1.jpg" alt="">
                                                            </div> -->
                                <div class="author-text">
                                  <h5 class="name">Dr.Andrew</h5>
                                  <span class="designation">Mavuno Clinic</span>
                                </div>
                              </div>
                              <div class="testimonial-quote">
                                <img
                                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/quote.png"
                                  alt=""
                                />
                              </div>
                            </div>
                          </div>
                        </div>
                        <!-- Single Testimonial End -->
                      </div>
                    </div>

                    <!-- Add Pagination -->
                    <div class="testimonial-arrow swiper-button-next"></div>
                    <div class="testimonial-arrow swiper-button-prev"></div>
                  </div>
                </div>
                <!-- Testimonial Slider Wrap End -->
              </div>
            </div>
          </div>
          <!-- Testimonial Wrap End -->
        </div>
      </div>
      <!-- Testimonial End -->

      <!-- About-2 End -->

      <!-- Video Start -->
      <!-- <div class="section video-section" style="background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/video-img.webp);">
            <div class="container">
                Video Wrap Start
                <div class="video-wrap">
                    <div class="row justify-content-center">
                        <div class="col-lg-8 col-md-10">
                            Video Content Start
                            <div class="video-content text-center">
                                <h2 class="title">We provide truly prominent IT solutions for your success</h2>
                                <div class="video-play">
                                    <a class="popup-video" href="https://www.youtube.com/watch?time_continue=3&v=_X0eYtY8T_U">
                                        <i class="fas fa-play"></i>
                                        <span>Watch Intro</span>
                                    </a>
                                </div>
                            </div>
                            Video Content End
                        </div>
                    </div>
                </div>
                Video Wrap End
            </div>
        </div> -->
      <!-- Video End -->

      <!-- Brand Logo Start -->
      <div class="section Brand-section Brand-section-2">
        <div class="container">
          <!-- Brand Wrapper Start -->
          <div class="brand-wrapper brand-wrapper-2 text-center">
            <h3 class="brand-title">
              Trusted by <span>Multiple</span> companies
            </h3>

            <!-- Brand Active Start -->
            <div class="brand-active">
              <div class="swiper-container">
                <div class="swiper-wrapper">
                  <!-- Single Brand Start -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/brand-1.jpg"
                      alt="Brand"
                      height="90"
                      width="150"
                    />
                  </div>
                  <!-- Single Brand End -->
                  <!-- Single Brand Start -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/brand-2.png"
                      alt="Brand"
                      height="115"
                      width="111"
                    />
                  </div>
                  <!-- Single Brand End -->
                  <!-- Single Brand Start -->
                  <!-- dentmind -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/dentmind.png"
                      alt="Brand"
                      height="115"
                      width="111"
                    />
                  </div>
                  <!-- Single Brand End -->
                  <!-- Single Brand Start -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/brand-13.jpg"
                      alt="Brand"
                      height="75"
                      width="115"
                    />
                  </div>
                  <!-- Single Brand End -->
                  <!-- Single Brand Start -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/brand-4.png"
                      alt="Brand"
                      height="115"
                      width="111"
                    />
                  </div>
                  <!-- moibentech -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/moiben-partner.png"
                      alt="Brand"
                      height="58"
                      width="190"
                    />
                  </div>
                  <!-- accessbank -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/logo-main.png"
                      alt="Brand"
                      height="45"
                      width="160"
                    />
                  </div>
                  <!-- mosoriottti -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/mosologo.png"
                      alt="Brand"
                      height="58"
                      width="190"
                    />
                  </div>
                  <!-- Single Brand End -->
                  <!-- Single Brand Start -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/pinnacle.webp"
                      alt="Brand"
                      height="115"
                      width="111"
                    />
                  </div>
                  <!-- Single Brand End -->
                  <!-- Single Brand Start -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/shemus.png"
                      alt="Brand"
                      height="115"
                      width="115"
                    />
                  </div>
                  <!-- Single Brand End -->
                  <!-- Single Brand Start -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/brand-7.png"
                      alt="Brand"
                      height="80"
                      width="150"
                    />
                  </div>
                  <!-- Single Brand End -->
                  <!-- Single Brand Start -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/brand-8.png"
                      alt="Brand"
                      height="115"
                      width="111"
                    />
                  </div>
                  <!-- Single Brand End -->
                  <!-- Single Brand Start -->
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/dianadental.png"
                      alt="Brand"
                      height="115"
                      width="111"
                    />
                  </div>
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/brand-10.png"
                      alt="Brand"
                      height="115"
                      width="111"
                    />
                  </div>
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/dentistltd.webp"
                      alt="Brand"
                      height="71"
                      width="190"
                    />
                  </div>
                  <div class="swiper-slide single-brand">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/brand/brand-12.png"
                      alt="Brand"
                      height="70"
                      width="140"
                    />
                  </div>
                  <!-- Single Brand End -->
                </div>
              </div>
            </div>
            <!-- Brand Active End -->
          </div>
          <!-- Brand Wrapper End -->
        </div>
      </div>
      <!-- Brand Logo End -->

      <!-- Cta Start -->
      <div
        class="section cta-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/cta-2-bg.jpg);
        "
      >
        <div class="container">
          <!-- Cta Wrap Start -->
          <div class="cta-wrap-2">
            <div class="row align-items-center">
              <div class="col-lg-6">
                <!-- Cta Content Start -->
                <div class="cta-content">
                  <h3 class="title">Start your journey with us</h3>
                </div>
                <!-- Cta Content End -->
              </div>
              <div class="col-lg-6">
                <!-- Cta Button Start -->
                <div class="cta-btn">
                  <a class="btn" href="mailto:info@lancolatech.co.ke"
                    >Request A Quote</a
                  >
                  <a class="btn btn-white" href="tel:254115588872"
                    >Call Us Now!</a
                  >
                </div>
                <!-- Cta Button End -->
              </div>
            </div>
          </div>
          <!-- Cta Wrap End -->
        </div>
      </div>
      <!-- Cta End -->

      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <!-- <div class="progress-wrap">
            <svg class="progress-circle svg-content" width="100%" height="100%" viewBox="-1 -1 102 102">
                <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
            </svg>
        </div> -->
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <!-- <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script> -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- WhatsApp START-->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/whatsapp/main.js"></script>
    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""

    return page


@app.route('/about')
def home():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>

    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://res.cloudinary.com/weknow-creators/image/upload/v1647694697/cropped-Lancola-Tech-Logo-PNG_r2ifii.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- <link rel="stylesheet" href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/vendor/plugins.min.css">
        <link rel="stylesheet" href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.min.css"> -->
  </head>

  <body>
    <div class="main-wrapper">
      <!-- Preloader start -->
      <!-- <div id="preloader">
            <div class="preloader">
                <span></span>
                <span></span>
            </div>
        </div> -->
      <!-- Preloader End -->

      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li class="active-menu">
                  <a href="about">About Us</a>
                </li>
                <li>
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <!-- Header Search Start -->
              <!-- Header Search End -->

              <!-- Header Cart Start -->

              <!-- Header Cart End -->
              <!-- Header Info Start -->
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li><a href="IT-consultation">IT Consultation</a></li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>
              <!-- <li><a href="team">Our Team</a></li> -->
              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->
      <div
        class="section case-study-section-2 section-padding"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/c-study-bg.jpg);
        "
      >
        <!-- <div class="container">
                <div class="case-study-wrap">
                    <div class="section-title text-center">
                        <h3 class="sub-title">management systems</h3>
                    </div>
                </div>
            </div> -->
        <!-- <div class="section-title text-center">
                        <br>
                        <h4>LANCOLATECH is a top-of-the line line of management systems provider, working as the primary tool to give you hope and happiness in your business.With our Management System, we provide you with easy-to-use tools for all your work structures. With one of the leading systems in the company, you can easily and quickly develop and integrate structuring within marketing, accounting or human resources. Our company is known for its outstanding performance in provision of C-POS, C-MED, C-DENT management systems across the country. </h4>
                    </div> -->
      </div>
      <!-- About Start -->
      <div class="section about-section section-padding">
        <div class="container">
          <!-- About Wrap Start -->
          <div class="about-wrap">
            <div class="row">
              <div class="col-lg-6">
                <!-- About Thumb Wrap Start -->
                <div class="about-thumb-wrap">
                  <div class="about-thumb-small">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/about-1.jpg"
                      alt=""
                    />
                  </div>
                  <div class="about-thumb-big">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/about-2.jpg"
                      alt=""
                    />
                  </div>
                  <div class="about-thumb-shape">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/ab-shape.png"
                      alt=""
                    />
                  </div>
                  <!-- <div class="play-btn">
                                    <a class="popup-video" href="https://www.youtube.com/watch?time_continue=3&v=_X0eYtY8T_U"><i class="fas fa-play"></i></a>
                                </div> -->
                </div>
                <!-- About Thumb Wrap End -->
              </div>
              <div class="col-lg-6">
                <!-- About Content Start -->
                <div class="about-content">
                  <div class="section-title">
                    <!-- <h3 class="sub-title">Who We Are</h3> -->
                    <h4>
                      LANCOLATECH is a top-of-the line line of management
                      systems provider, working as the primary tool to give you
                      hope and happiness in your business.With our Management
                      System, we provide you with easy-to-use tools for all your
                      work structures. <br /><br />
                      With one of the leading systems in the company, you can
                      easily and quickly develop and integrate structuring
                      within marketing, accounting or human resources. Our
                      company is known for its outstanding performance in
                      provision of C-POS, C-MED, C-DENT management systems
                      across the country.
                    </h4>
                  </div>
                  <!-- <p><strong>LancolaTech Company</strong> was established in response to a growing niche market for IT
                                    solution within diverse sectors including government, non-governmental rganizations,
                                    cooperatives, and state corporations, private industrial and commercial corporations; Among other
                                    consumers of products and services.</p> -->
                </div>
                <!-- About Content End -->
              </div>
            </div>
          </div>
          <!-- About Wrap End -->
        </div>
      </div>
      <!-- About End -->

      <!-- Service Start -->
      <div class="section service-section service-section-5">
        <div class="container">
          <div class="service-wrap">
            <div class="row">
              <div class="col-lg-4 col-sm-6">
                <!-- Service Item Start -->
                <div class="service-item about-service-item text-center">
                  <div class="shape-1"></div>
                  <div class="shape-2">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/s-shape-2.png"
                      alt=""
                    />
                  </div>
                  <div class="service-icon">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/service-1.png"
                      alt=""
                    />
                  </div>
                  <div class="service-content">
                    <h3 class="title"><a href="#">Mission</a></h3>
                    <p>
                      To provide practical innovative and cutting edgesolutions
                      to our clients diverse supply chain requirements by
                      delivering quality value efficiencies in our products and
                      services.
                    </p>
                  </div>
                </div>
                <!-- Service Item End -->
              </div>
              <div class="col-lg-4 col-sm-6">
                <!-- Service Item Start -->
                <div class="service-item about-service-item text-center">
                  <div class="shape-1"></div>
                  <div class="shape-2">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/s-shape-2.png"
                      alt=""
                    />
                  </div>
                  <div class="service-icon">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/service-2.png"
                      alt=""
                    />
                  </div>
                  <div class="service-content">
                    <h3 class="title"><a href="#">Vision</a></h3>
                    <p>
                      To be an outstanding brand and market leader provider in
                      “IT Solutions provision “of quality services synonymous
                      with reliability, integrity and success.
                    </p>
                  </div>
                </div>
                <!-- Service Item End -->
              </div>
              <div class="col-lg-4 col-sm-6">
                <!-- Service Item Start -->
                <div class="service-item about-service-item text-center">
                  <div class="shape-1"></div>
                  <div class="shape-2">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/s-shape-2.png"
                      alt=""
                    />
                  </div>
                  <div class="service-icon">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/service-3.png"
                      alt=""
                    />
                  </div>
                  <div class="service-content">
                    <h3 class="title"><a href="#">Our Objectives</a></h3>
                    <ul>
                      <li>
                        To exceed customer expectations through continuous
                        improvement in quality, service productivity and time
                        compression.
                      </li>
                      <li>To build long term partnership with our clients.</li>
                    </ul>
                  </div>
                </div>
                <!-- Service Item End -->
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Service End -->

      <!--  Skill Start -->
      <div class="section skill-section skill-section-2">
        <div class="container">
          <div class="skill-wrap">
            <!--  Skill Content Wrap Start -->
            <div class="skill-content-wrap">
              <div class="row align-items-center">
                <div class="col-lg-5">
                  <!--  Skill Content Left Start -->
                  <div class="skill-content-left">
                    <div class="experience">
                      <h2 class="number">6+</h2>
                      <span>Years of experience</span>
                    </div>
                    <h3 class="title">
                      We run all kinds of <span>IT services</span> that vow your
                      success
                    </h3>
                  </div>
                  <!--  Skill Content Left End -->
                </div>
                <div class="col-lg-7">
                  <!--  Skill Content Right Start -->
                  <div class="skill-content-right">
                    <h3 class="title">
                      Accelerate innovation with world-class tech teams We’ll
                      match you to an entire remote technology
                    </h3>
                    <div class="skill-bar-wrap">
                      <!--  Skill Item Start  -->
                      <div class="skill-item">
                        <div class="skill-header">
                          <h5 class="skill-title">IT Managment</h5>
                          <span class="skill-percentage">
                            <span class="counter">90</span>
                            %
                          </span>
                        </div>
                        <div class="skill-bar">
                          <div class="bar-inner">
                            <div class="progress-line" data-width="90"></div>
                          </div>
                        </div>
                      </div>
                      <!--  Skill Item End  -->
                      <!--  Skill Item Start  -->
                      <div class="skill-item">
                        <div class="skill-header">
                          <h5 class="skill-title">Data Security</h5>
                          <span class="skill-percentage">
                            <span class="counter">90</span>
                            %
                          </span>
                        </div>
                        <div class="skill-bar">
                          <div class="bar-inner">
                            <div class="progress-line" data-width="90"></div>
                          </div>
                        </div>
                      </div>
                      <!--  Skill Item End  -->
                      <!--  Skill Item Start  -->
                      <div class="skill-item">
                        <div class="skill-header">
                          <h5 class="skill-title">Solutions</h5>
                          <span class="skill-percentage">
                            <span class="counter">95</span>
                            %
                          </span>
                        </div>
                        <div class="skill-bar">
                          <div class="bar-inner">
                            <div class="progress-line" data-width="90"></div>
                          </div>
                        </div>
                      </div>
                      <!--  Skill Item End  -->
                    </div>
                  </div>
                  <!--  Skill Content Right End -->
                </div>
              </div>
            </div>
            <!--  Skill Content Wrap End -->
          </div>
        </div>
      </div>
      <!--  Skill End -->

      <!-- Counter Start -->
      <div
        class="section counter-section"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/counter-bg.jpg);
        "
      >
        <div class="container">
          <div class="counter-wrap">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Counter Item Start -->
                <div class="counter-item text-center">
                  <div class="counter-icon">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/counter/counter-1.png"
                      alt=""
                    />
                  </div>
                  <div class="counter-text">
                    <span> <span class="counter">10</span>+ </span>
                    <p>Completed Projects</p>
                  </div>
                </div>
                <!-- Counter Item End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Counter Item Start -->
                <div class="counter-item text-center">
                  <div class="counter-icon">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/counter/counter-2.png"
                      alt=""
                    />
                  </div>
                  <div class="counter-text">
                    <span> <span class="counter">100</span>+ </span>
                    <p>Satisfied Clients</p>
                  </div>
                </div>
                <!-- Counter Item End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Counter Item Start -->
                <div class="counter-item text-center">
                  <div class="counter-icon">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/counter/counter-3.png"
                      alt=""
                    />
                  </div>
                  <div class="counter-text">
                    <span> <span class="counter">50</span>+ </span>
                    <p>Websites Designed</p>
                  </div>
                </div>
                <!-- Counter Item End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Counter Item Start -->
                <div class="counter-item text-center">
                  <div class="counter-icon">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/counter/counter-4.png"
                      alt=""
                    />
                  </div>
                  <div class="counter-text">
                    <span> <span class="counter">100</span>+ </span>
                    <p>Clients Supoort Done</p>
                  </div>
                </div>
                <!-- Counter Item End -->
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Counter End -->

      <!-- Testimonial Start -->

      <!-- Testimonial End -->

      <!-- Brand Logo Start -->

      <!-- Brand Logo End -->

      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <div class="progress-wrap">
        <svg
          class="progress-circle svg-content"
          width="100%"
          height="100%"
          viewBox="-1 -1 102 102"
        >
          <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
        </svg>
      </div>
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


@app.route('/bulk-sms')
def bulk_sms():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>
    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />

    <style>
      .pop-out {
        transition: transform 0.5s;
      }

      .pop-out:hover {
        -ms-transform: scale(2, 2);
        -webkit-transform: scale(2, 2);
        transform: scale(2, 2);
      }
    </style>
  </head>
  <body>
    <div class="main-wrapper">
      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li class="active-menu">
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li class="active-menu">
                      <a href="bulk-sms">Bulk SMS</a>
                    </li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>
              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <!-- Case Study Start -->
      <div class="section case-study-section-2 section-padding">
        <div class="container">
          <!-- Case Study Wrap Start -->
          <div class="case-study-wrap">
            <div class="section-title text-center">
              <br />
              <br />
              <br />
              <h3 class="sub-title">bulk sms</h3>
              <h4>
                LancolaSMS is an award-winning Bulk SMS Service Provider in
                Kenya. We provide customized bulk SMS, SMS gateway, free SMS
                API, free SMS software and bulk data bundles to our customers at
                the most affordable rates. Our best bulk SMS offer comes with no
                extra cost for sending bulk SMS in Kenya as a part of your
                business growth plan to build your brand Awareness, Sales or for
                marketing purposes or even for fun or create loyalty among your
                customers. LancolaSMS offers cost-effective and accurate bulk
                SMS messaging solutions that help you achieve your business
                goals. We are one of the top bulk SMS service providers
                providing wide range of bulk SMS services.
              </h4>
            </div>

            <div class="case-study-content-wrap">
              <div class="row">
                <div class="col-lg-4 col-md-6">
                  <div class="case-study-item">
                    <div class="case-study-img">
                      <a href="#"
                        ><img
                          class="pop-out"
                          src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/SCREEN SHOT FOR THE BULKS SMS.PNG"
                          alt=""
                      /></a>
                    </div>
                    <div class="case-study-content">
                      <h3 class="title"><a href="javacript:;">Bulk-SMS</a></h3>
                      <!-- <span>Point of sale system</span> -->
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Case Study End -->

      <div class="section about-section section-padding">
        <div class="container">
          <!-- About Wrap Start -->
          <div class="about-wrap">
            <div class="row">
              <div class="col-lg-6">
                <!-- About Thumb Wrap Start -->
                <div class="about-thumb-wrap">
                  <div class="about-thumb-small">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/pixlr-bg-result234.png"
                      alt=""
                      height="250"
                    />
                  </div>
                  <div class="about-thumb-big">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/clipart1515675.png"
                      alt=""
                      height="265"
                      width="300"
                    />
                  </div>
                  <div class="about-thumb-shape">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/ab-shape.png"
                      alt=""
                    />
                  </div>
                  <!-- <div class="play-btn">
                                    <a class="popup-video" href="https://www.youtube.com/watch?time_continue=3&v=_X0eYtY8T_U"><i class="fas fa-play"></i></a>
                                </div> -->
                </div>
                <!-- About Thumb Wrap End -->
              </div>
              <div class="col-lg-6">
                <!-- About Content Start -->
                <div class="about-content">
                  <div class="section-title">
                    <h3 class="sub-title">Bulk SMS</h3>
                    <h4>
                      Our powerful SMS API offers a platform for you to send
                      productive text messages to your customers, patients,
                      students and more.
                    </h4>
                  </div>
                  <p>
                    Our easy to use SMS APIs provides a variety of ways for you
                    to add text messaging service to your mobile and web
                    applications. You will be able to draw the attention of your
                    customers, remind patients on their appointments and
                    medications, prompt students on examination dates, Fee
                    payments and Events
                  </p>
                </div>
                <!-- About Content End -->
              </div>
            </div>
          </div>
          <!-- About Wrap End -->
        </div>
      </div>
      <!-- Features Start -->
      <div
        class="section features-section-3 features-section-4 section-padding"
      >
        <!-- Footer Section Start -->
        <div
          class="section footer-section footer-section-2"
          style="
            background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
          "
        >
          <div class="container">
            <!-- Footer Widget Wrap Start -->
            <div class="footer-widget-wrap footer-widget-wrap-2">
              <div class="row">
                <div class="col-lg-3 col-sm-6">
                  <!-- Footer Widget Start -->
                  <div class="footer-widget-about">
                    <a class="footer-logo" href="/"
                      ><img
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                        alt="Logo"
                    /></a>
                    <div class="widget-info widget-info-2">
                      <ul>
                        <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                        <li>
                          <div class="info-icon">
                            <i class="far fa-envelope-open"></i>
                          </div>
                          <div class="info-text">
                            <span
                              ><a href="mailto:info@lancolatech.co.ke"
                                >info@lancolatech.co.ke</a
                              ></span
                            >
                          </div>
                        </li>
                        <li>
                          <div class="info-icon">
                            <i class="flaticon-pin"></i>
                          </div>
                          <div class="info-text">
                            <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                  <!-- Footer Widget End -->
                </div>
                <div class="col-lg-3 col-sm-6">
                  <!-- Footer Widget Start -->
                  <div class="footer-widget footer-widget-2">
                    <h4 class="footer-widget-title">Useful Links</h4>

                    <div class="widget-link">
                      <ul class="link">
                        <li>
                          <a href="terms-and-conditions.txt" target="_blank"
                            >Terms & Conditions</a
                          >
                        </li>
                        <li>
                          <a href="https://blog.lancolatech.co.ke">Blog</a>
                        </li>
                        <!-- <li><a href="support">Support</a></li> -->
                      </ul>
                    </div>
                  </div>
                  <!-- Footer Widget End -->
                </div>
              </div>
            </div>
            <!-- Footer Widget Wrap End -->
          </div>

          <!-- Footer Copyright Start -->
          <div class="footer-copyright-area footer-copyright-2">
            <div class="container">
              <div class="footer-copyright-wrap">
                <div class="row align-items-center">
                  <div class="col-lg-6 col-md-6">
                    <!-- Footer Copyright Text Start -->
                    <div class="copyright-text">
                      <p>
                        <strong>
                          &copy; <span id="copyright-year"></span>
                          <script>
                            document.querySelector(
                              "#copyright-year"
                            ).innerText = new Date().getFullYear();
                          </script>
                          Lancolatech</strong
                        >
                      </p>
                    </div>
                    <!-- Footer Copyright Text End -->
                  </div>
                  <div class="col-lg-6 col-md-6">
                    <!-- Footer Copyright Social Start -->
                    <div class="copyright-social">
                      <ul class="social">
                        <li>
                          <a
                            href="https://www.facebook.com/Lancola-Tech-246152853989129"
                            target="_blank"
                            ><i class="fab fa-facebook-f"></i
                          ></a>
                        </li>
                        <li>
                          <a href="https://twitter.com/lancolatech"
                            ><i class="fab fa-twitter"></i
                          ></a>
                        </li>
                        <li>
                          <a href="https://www.instagram.com/lancolatech/"
                            ><i class="fab fa-instagram"></i
                          ></a>
                        </li>
                        <li>
                          <a href="https://linkedin.com/in/lancolatech"
                            ><i class="fab fa-linkedin-in"></i
                          ></a>
                        </li>
                      </ul>
                    </div>
                    <!-- Footer Copyright Social End -->
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Footer Copyright End -->
        </div>
        <!-- Footer Section End -->

        <!-- back to top start -->
        <div class="progress-wrap">
          <svg
            class="progress-circle svg-content"
            width="100%"
            height="100%"
            viewBox="-1 -1 102 102"
          >
            <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
          </svg>
        </div>
        <!-- back to top end -->
      </div>

      <!-- JS
    ============================================ -->
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

      <!-- Bootstrap JS -->
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

      <!-- Plugins JS -->
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

      <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
      <!-- tawk.to -->
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

      <!-- Main JS -->
      <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>

      <!-- </body> -->
      <!-- </html> -->
    </div>
  </body>
</html>
"""
    return page


@app.route('/CCTV-installations')
def CCTV_installations():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>

    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />
  </head>
  <body>
    <div class="main-wrapper">
      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li class="active-menu">
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li class="active-menu">
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <!-- Header Search Start -->
              <!-- Header Search End -->

              <!-- Header Cart Start -->

              <!-- Header Cart End -->
              <!-- Header Info Start -->
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>
              <!-- <li><a href="team">Our Team</a></li> -->
              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <!-- Case Study Start -->
      <div class="section case-study-section-2 section-padding">
        <div class="container">
          <!-- Case Study Wrap Start -->
          <div class="case-study-wrap">
            <div class="section-title text-center">
              <br />
              <br />
              <br />
              <h3 class="sub-title">CCTV InstalltionS</h3>
              <h4>
                At LANCOLATECH COMPANY, we specialize in home and business
                security systems. From a simple home network to CCTV cameras, we
                service all types of installations. With our experience security
                technical team, we are here to help you out with your home or
                business security needs. We specialize in high quality
                electronic products that are affordable and long-lasting.
              </h4>
            </div>
            <!-- Case Study Content Wrap Start -->
            <!-- <div class="case-study-content-wrap">
                        <div class="row">
                            <div class="col-lg-4 col-md-6">
                                <div class="case-study-item">
                                    <div class="case-study-img">
                                        <a href="#"><img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-study-4.jpg" alt=""></a>
                                    </div>
                                    <div class="case-study-content">
                                        <h3 class="title"><a href="#">C-pos</a></h3>
                                        <span>Point of sale system</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6">
                                <div class="case-study-item">
                                    <div class="case-study-img">
                                        <a href="#"><img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-study-5.jpg" alt=""></a>
                                    </div>
                                    <div class="case-study-content">
                                        <h3 class="title"><a href="#">C-dent</a></h3>
                                        <span>Dental clinic system</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6">
                                <div class="case-study-item">
                                    <div class="case-study-img">
                                        <a href="#"><img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-study-6.jpg" alt=""></a>
                                    </div>
                                    <div class="case-study-content">
                                        <h3 class="title"><a href="#">C-med</a></h3>
                                        <span>Medical facility system</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div> -->
            <!-- Case Study Content Wrap End -->
          </div>
          <!-- Case Study Wrap End -->
        </div>
        <!-- <div class="section-title text-center">
                        <br>
                        <h4>At LANCOLATECH COMPANY, we specialize in home and business security systems. From a simple home network to CCTV cameras, we service all types of installations. With our experience security technical team, we are here to help you out with your home or business security needs. We specialize in high quality electronic products that are affordable and long-lasting.</h4>
                    </div> -->
      </div>
      <!-- Case Study End -->

      <div class="section about-section section-padding">
        <div class="container">
          <!-- About Wrap Start -->
          <div class="about-wrap">
            <div class="row">
              <div class="col-lg-6">
                <!-- About Thumb Wrap Start -->
                <div class="about-thumb-wrap">
                  <div class="about-thumb-small">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/V0PR_132186271948336166C3U3h1z2YC.jpg"
                      alt=""
                      height="307"
                      width="410"
                    />
                  </div>
                  <div class="about-thumb-big">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/A98Y_1_20180521856128876-new.png"
                      alt=""
                      height="250"
                      width="333"
                    />
                  </div>
                  <div class="about-thumb-shape">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/ab-shape.png"
                      alt=""
                    />
                  </div>
                </div>
                <!-- About Thumb Wrap End -->
              </div>
              <div class="col-lg-6">
                <!-- About Content Start -->
                <div class="about-content">
                  <div class="section-title">
                    <h3 class="sub-title">CCTV installation</h3>
                    <h4>
                      We offer exceptional cctv installation services to protect
                      people, property and
                      https://ver-vite.assets.cdn.lancolatech.co.ke/assets. With
                      our service, we provide a solution to possible danger,
                      damage loss and criminal activities against with you
                      premises.
                    </h4>
                  </div>
                  <p>
                    LancolaTech has a group of expert Technicians in CCTV camera
                    installation. We build reliable CCTV Network in Hospitals,
                    Schools, Offices and Company premises.
                  </p>
                  <br />
                  <br />
                  <br />
                  <br />
                </div>
                <!-- About Content End -->
              </div>
            </div>
          </div>
          <!-- About Wrap End -->
        </div>
      </div>

      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <div class="progress-wrap">
        <svg
          class="progress-circle svg-content"
          width="100%"
          height="100%"
          viewBox="-1 -1 102 102"
        >
          <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
        </svg>
      </div>
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


@app.route('/computer-accessories')
def computer_accessories():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>

    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- <link rel="stylesheet" href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/vendor/plugins.min.css">
        <link rel="stylesheet" href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.min.css"> -->
  </head>

  <body>
    <div class="main-wrapper">
      <!-- Preloader start -->
      <!-- <div id="preloader">
            <div class="preloader">
                <span></span>
                <span></span>
            </div>
        </div> -->
      <!-- Preloader End -->

      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li class="active-menu">
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li class="active-menu">
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <!-- Header Search Start -->
              <!-- Header Search End -->

              <!-- Header Cart Start -->

              <!-- Header Cart End -->
              <!-- Header Info Start -->
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="container">
          <div class="features-wrap-3">
            <div class="section-title2 text-center">
              <h2 class="title">
                Effortlessly send <span>Bulk SMS</span>across Kenya
              </h2>
              <br />
              <br />
              <h3>Supported Networks in Kenya</h3>
              <br />
              <br />
              <img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/solution-network.png"
                alt=""
                height="36"
                width="50"
              />
              <h3>Airtel</h3>
              <img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/solution-network.png"
                alt=""
                height="36"
                width="50"
              />
              <h3>Telkom</h3>
              <img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/solution-network.png"
                alt=""
                height="36"
                width="50"
              />
              <h3>Safaricom</h3>
              <img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/solution-network.png"
                alt=""
                height="36"
                width="50"
              />
              <h3>Jamii Telecom (Faiba)</h3>
            </div>
          </div>
        </div>
        <div class="offcanvas-menu">
          <ul class="main-menu">
            <li class="active-menu">
              <a href="/">Home</a>
            </li>
            <li>
              <a href="about">About Us</a>
            </li>
            <li>
              <a href="javascript:;">Our Services</a>
              <ul class="sub-menu">
                <li><a href="bulk-sms">Bulk SMS</a></li>
                <li>
                  <a href="management-systems">Management Systems</a>
                </li>
                <li>
                  <a href="computer-solutions-and-consultancy"
                    >Computer Solutions & Consultancy</a
                  >
                </li>
                <li>
                  <a href="computer-accessories">Computer Accessories</a>
                </li>
                <li><a href="CCTV-installations">CCTV Installtions</a></li>
                <li>
                  <a href="structured-cabling-and-networking"
                    >Structured Cabling and Networking</a
                  >
                </li>
                <li><a href="digital-marketing">Digital Marketing</a></li>
                <li><a href="web-development">Web Development</a></li>
                <li>
                  <a href="computer-solutions-and-consultancy"
                    >Computer Solutions & Consultancy</a
                  >
                </li>
              </ul>
            </li>
            <li>
              <a href="https://blog.lancolatech.co.ke" target="_blank">Blog</a>
            </li>
            <!-- <li><a href="team">Our Team</a></li> -->
            <li><a href="contact">Contact</a></li>
          </ul>
        </div>
      </div>
      <!-- Offcanvas Body End -->
    </div>
    <!-- Offcanvas End -->

    <!-- Case Study Start -->
    <div class="section case-study-section-2 section-padding">
      <div class="container">
        <!-- Case Study Wrap Start -->
        <div class="case-study-wrap">
          <div class="section-title text-center">
            <br />
            <br />
            <br />
            <h3 class="sub-title">Computer accessories</h3>
            <h4>
              Lancolatech is a reliable Computer Accessories seller in Eldoret,
              Kenya. We strive to ensure our customers know exactly what they
              are buying, with the best prices and product quality from the
              trusted Computer Accessories suppliers. We have built a proven
              track record on variety, best prices and speedy delivery.
            </h4>
          </div>
          <!-- Case Study Content Wrap Start -->
          <!-- <div class="case-study-content-wrap">
                        <div class="row">
                            <div class="col-lg-4 col-md-6">
                                <div class="case-study-item">
                                    <div class="case-study-img">
                                        <a href="#"><img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-study-4.jpg" alt=""></a>
                                    </div>
                                    <div class="case-study-content">
                                        <h3 class="title"><a href="#">C-pos</a></h3>
                                        <span>Point of sale system</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6">
                                <div class="case-study-item">
                                    <div class="case-study-img">
                                        <a href="#"><img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-study-5.jpg" alt=""></a>
                                    </div>
                                    <div class="case-study-content">
                                        <h3 class="title"><a href="#">C-dent</a></h3>
                                        <span>Dental clinic system</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6">
                                <div class="case-study-item">
                                    <div class="case-study-img">
                                        <a href="#"><img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-study-6.jpg" alt=""></a>
                                    </div>
                                    <div class="case-study-content">
                                        <h3 class="title"><a href="#">C-med</a></h3>
                                        <span>Medical facility system</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div> -->
          <!-- Case Study Content Wrap End -->
        </div>
        <!-- Case Study Wrap End -->
      </div>
      <!-- <div class="section-title text-center">
                        <br>
                        <h4>Lancolatech is a reliable Computer Accessories seller in Eldoret, Kenya. We strive to ensure our customers know exactly what they are buying, with the best prices and product quality from the trusted Computer Accessories suppliers. We have built a proven track record on variety, best prices and speedy delivery.</h4>
                    </div> -->
    </div>
    <!-- Case Study End -->

    <div class="section about-section section-padding">
      <div class="container">
        <!-- About Wrap Start -->
        <div class="about-wrap">
          <div class="row">
            <div class="col-lg-6">
              <!-- About Thumb Wrap Start -->
              <div class="about-thumb-wrap">
                <div class="about-thumb-small">
                  <img
                    src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/pixlr-bg-result (1).png"
                    alt=""
                    height="250"
                  />
                </div>
                <div class="about-thumb-big">
                  <img
                    src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/pixlr-bg-result (2).png"
                    alt=""
                    height="225"
                    width="300"
                  />
                </div>
                <div class="about-thumb-shape">
                  <img
                    src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/ab-shape.png"
                    alt=""
                  />
                </div>
                <!-- <div class="play-btn">
                                    <a class="popup-video" href="https://www.youtube.com/watch?time_continue=3&v=_X0eYtY8T_U"><i class="fas fa-play"></i></a>
                                </div> -->
              </div>
              <!-- About Thumb Wrap End -->
            </div>
            <div class="col-lg-6">
              <!-- About Content Start -->
              <div class="about-content">
                <div class="section-title">
                  <h3 class="sub-title">computer accessories</h3>
                  <h4>
                    We sell quality and Affordable Laptops, Laptops' accessories
                    and Computer Repair Services to Residential and Commercial
                    customers.
                  </h4>
                </div>
                <p>Some of the procucts we sell include:</p>
                <ul>
                  <strong>
                    <li>Keyboards</li>
                    <li>Mice</li>
                    <li>Printers</li>
                    <li>Monitors</li>
                    <li>Desktops</li>
                    <li>Laptops</li>
                    <li>Ink catridges</li>
                    <li>USB Flash Drives</li>
                    <li>USB Chargers</li>
                    <li>USB Cables</li>
                    <li>USB Chargers</li>
                    <li>Webcams</li>
                  </strong>
                </ul>
              </div>
              <!-- About Content End -->
            </div>
          </div>
        </div>
        <!-- About Wrap End -->
      </div>
    </div>

    <!-- Footer Section Start -->
    <div
      class="section footer-section footer-section-2"
      style="
        background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
      "
    >
      <div class="container">
        <!-- Footer Widget Wrap Start -->
        <div class="footer-widget-wrap footer-widget-wrap-2">
          <div class="row">
            <div class="col-lg-3 col-sm-6">
              <!-- Footer Widget Start -->
              <div class="footer-widget-about">
                <a class="footer-logo" href="/"
                  ><img
                    src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                    alt="Logo"
                /></a>
                <div class="widget-info widget-info-2">
                  <ul>
                    <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                    <li>
                      <div class="info-icon">
                        <i class="far fa-envelope-open"></i>
                      </div>
                      <div class="info-text">
                        <span
                          ><a href="mailto:info@lancolatech.co.ke"
                            >info@lancolatech.co.ke</a
                          ></span
                        >
                      </div>
                    </li>
                    <li>
                      <div class="info-icon">
                        <i class="flaticon-pin"></i>
                      </div>
                      <div class="info-text">
                        <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <!-- Footer Widget End -->
            </div>
            <div class="col-lg-3 col-sm-6">
              <!-- Footer Widget Start -->
              <div class="footer-widget footer-widget-2">
                <h4 class="footer-widget-title">Useful Links</h4>

                <div class="widget-link">
                  <ul class="link">
                    <li>
                      <a href="terms-and-conditions.txt" target="_blank"
                        >Terms & Conditions</a
                      >
                    </li>
                    <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                    <!-- <li><a href="support">Support</a></li> -->
                  </ul>
                </div>
              </div>
              <!-- Footer Widget End -->
            </div>
          </div>
        </div>
        <!-- Footer Widget Wrap End -->
      </div>

      <!-- Footer Copyright Start -->
      <div class="footer-copyright-area footer-copyright-2">
        <div class="container">
          <div class="footer-copyright-wrap">
            <div class="row align-items-center">
              <div class="col-lg-6 col-md-6">
                <!-- Footer Copyright Text Start -->
                <div class="copyright-text">
                  <p>
                    <strong>
                      &copy; <span id="copyright-year"></span>
                      <script>
                        document.querySelector("#copyright-year").innerText =
                          new Date().getFullYear();
                      </script>
                      Lancolatech</strong
                    >
                  </p>
                </div>
                <!-- Footer Copyright Text End -->
              </div>
              <div class="col-lg-6 col-md-6">
                <!-- Footer Copyright Social Start -->
                <div class="copyright-social">
                  <ul class="social">
                    <li>
                      <a
                        href="https://www.facebook.com/Lancola-Tech-246152853989129"
                        target="_blank"
                        ><i class="fab fa-facebook-f"></i
                      ></a>
                    </li>
                    <li>
                      <a href="https://twitter.com/lancolatech"
                        ><i class="fab fa-twitter"></i
                      ></a>
                    </li>
                    <li>
                      <a href="https://www.instagram.com/lancolatech/"
                        ><i class="fab fa-instagram"></i
                      ></a>
                    </li>
                    <li>
                      <a href="https://linkedin.com/in/lancolatech"
                        ><i class="fab fa-linkedin-in"></i
                      ></a>
                    </li>
                  </ul>
                </div>
                <!-- Footer Copyright Social End -->
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Footer Copyright End -->
    </div>
    <!-- Footer Section End -->

    <!-- back to top start -->
    <div class="progress-wrap">
      <svg
        class="progress-circle svg-content"
        width="100%"
        height="100%"
        viewBox="-1 -1 102 102"
      >
        <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
      </svg>
    </div>
    <!-- back to top end -->
    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


@app.route('/computer-solutions-and-consultancy')
def computer_solutions_and_consultancy():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>

    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />
  </head>

  <body>
    <div class="main-wrapper">
      <!-- Preloader start -->
      <!-- <div id="preloader">
            <div class="preloader">
                <span></span>
                <span></span>
            </div>
        </div> -->
      <!-- Preloader End -->

      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li class="active-menu">
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li class="active-menu">
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <!-- Header Search Start -->
              <!-- Header Search End -->

              <!-- Header Cart Start -->

              <!-- Header Cart End -->
              <!-- Header Info Start -->
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>
              <!-- <li><a href="team">Our Team</a></li> -->
              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <!-- Case Study Start -->
      <div class="section case-study-section-2 section-padding">
        <div class="container">
          <!-- Case Study Wrap Start -->
          <div class="case-study-wrap">
            <div class="section-title text-center">
              <br />
              <br />
              <br />
              <h3 class="sub-title">
                computer computer solutions and consultancy
              </h3>
              <h4>
                We are your most trusted IT solutions partner. At LANCOLATECH
                COMPANY, we embrace new technology to create opportunities that
                deliver value to organizations we serve. We deliver leading IT
                infrastructure support, UPS power back up and Racks solutions
                for enterprise IT systems resilience, and corporate printer
                repair and maintenance services. Our top priority is delivering
                proven solutions that meet your organization’s business needs
                through engaging service levels, responsive project management
                and highly experienced technicians.
              </h4>
            </div>
          </div>
          <!-- Case Study Wrap End -->
        </div>
        <!-- <div class="section-title text-center">
                        <br>
                        <h4>We are your most trusted IT solutions partner. At LANCOLATECH COMPANY, we embrace new technology to create opportunities that deliver value to organizations we serve. We deliver leading IT infrastructure support, UPS power back up and Racks solutions for enterprise IT systems resilience, and corporate printer repair and maintenance services. Our top priority is delivering proven solutions that meet your organization’s business needs through engaging service levels, responsive project management and highly experienced technicians.</h4>
                    </div> -->
      </div>
      <!-- Case Study End -->

      <div class="section about-section section-padding">
        <div class="container">
          <!-- About Wrap Start -->
          <div class="about-wrap">
            <div class="row">
              <div class="col-lg-6">
                <!-- About Thumb Wrap Start -->
                <div class="about-thumb-wrap">
                  <div class="about-thumb-small">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/pixlr-bg-result567.png"
                      alt=""
                      height="300"
                    />
                  </div>
                  <div class="about-thumb-big">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/32-350-882-V01 (1).png"
                      alt=""
                      height="225"
                      width="300"
                    />
                  </div>
                  <div class="about-thumb-shape">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/ab-shape.png"
                      alt=""
                    />
                  </div>
                  <!-- <div class="play-btn">
                                    <a class="popup-video" href="https://www.youtube.com/watch?time_continue=3&v=_X0eYtY8T_U"><i class="fas fa-play"></i></a>
                                </div> -->
                </div>
                <!-- About Thumb Wrap End -->
              </div>
              <div class="col-lg-6">
                <!-- About Content Start -->
                <div class="about-content">
                  <div class="section-title">
                    <h3 class="sub-title">
                      computer computer solutions and consultancy
                    </h3>
                    <h4>
                      We sell a variety of computer solution ranging from:
                    </h4>
                  </div>
                  <p>
                    <strong
                      >Antivirus installation
                      <br />
                      <strong>Software and System upgrades</strong>
                      <strong>Account recovery</strong>
                      <strong>Data Recovery</strong>
                      <strong>Operating system installation :</strong>
                      <ol>
                        <li>Windows 11</li>
                        <li>Windows 10</li>
                        <li>Linux Systems</li>
                        <li>OSX Operating systems</li>
                        <li>Servers</li>
                      </ol>
                    </strong>
                  </p>
                  <br />
                </div>
                <!-- About Content End -->
              </div>
            </div>
          </div>
          <!-- About Wrap End -->
        </div>
      </div>
      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <div class="progress-wrap">
        <svg
          class="progress-circle svg-content"
          width="100%"
          height="100%"
          viewBox="-1 -1 102 102"
        >
          <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
        </svg>
      </div>
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


@app.route('/contact')
def contact():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>

    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <!-- <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    /> -->
    <!-- CSS only -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65"
      crossorigin="anonymous"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />

    <script src="https://js.hcaptcha.com/1/api.js" async defer></script>
  </head>

  <body>
    <div class="main-wrapper">
      <!-- Preloader start -->
      <!-- <div id="preloader">
            <div class="preloader">
                <span></span>
                <span></span>
            </div>
        </div> -->
      <!-- Preloader End -->

      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li>
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li class="active-menu"><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <!-- Header Search Start -->
              <!-- Header Search End -->

              <!-- Header Cart Start -->

              <!-- Header Cart End -->
              <!-- Header Info Start -->
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="#">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>

              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <!-- Contact Info Start -->
      <div class="section contact-info-section section-padding-02">
        <div class="container">
          <!-- Contact Info Wrap Start -->
          <br />
          <br />
          <br />
          <br />
          <div class="contact-info-wrap">
            <div class="row">
              <div class="col-lg-4 col-sm-6">
                <!--Single Contact Info Start -->
                <div class="single-contact-info text-center">
                  <div class="info-icon">
                    <i class="flaticon-phone-call"></i>
                  </div>
                  <div class="info-content">
                    <h5 class="title">Telephone</h5>
                    <p>+254 115 588 872</p>
                  </div>
                </div>
                <!--Single Contact Info End -->
              </div>
              <div class="col-lg-4 col-sm-6">
                <!--Single Contact Info Start -->
                <div class="single-contact-info text-center">
                  <div class="info-icon">
                    <i class="flaticon-email"></i>
                  </div>
                  <div class="info-content">
                    <h5 class="title">Mail Address</h5>
                    <p>info@lancolatech.co.ke</p>
                  </div>
                </div>
                <!--Single Contact Info End -->
              </div>
              <div class="col-lg-4 col-sm-6">
                <!--Single Contact Info Start -->
                <div class="single-contact-info text-center">
                  <div class="info-icon">
                    <i class="flaticon-pin"></i>
                  </div>
                  <div class="info-content">
                    <h5 class="title">Location</h5>
                    <p>Grand Pri 3rd Floor Room 301, Eldoret</p>
                  </div>
                </div>
                <!--Single Contact Info End -->
              </div>
            </div>
          </div>
          <!-- Contact Info Wrap End -->
        </div>
      </div>
      <!-- Contact Info End -->

      <!-- Contact Form Start -->
      <div class="section contact-form-section section-padding">
        <div class="container">
          <div class="contact-wrap">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <div class="form-title text-center">
                  <h2 class="title">Get Support from our Team</h2>
                </div>
                <!-- <form > -->
                <div class="contact-form-wrap">
                  <form action="https://api.web3forms.com/submit" method="POST">
                    <input
                      type="hidden"
                      name="access_key"
                      value="f494a78f-fbd7-474a-aae0-4ee175de7781"
                    />
                    <div class="row">
                      <div class="col-md-6">
                        <div class="single-form">
                          <input
                            class="form-control"
                            type="text"
                            placeholder="Your Name"
                            id="name"
                            name="name"
                            required
                          />
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="single-form">
                          <input
                            class="form-control"
                            type="email"
                            placeholder="Your Email"
                            id="email"
                            name="email"
                            required
                          />
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="single-form">
                          <input
                            class="form-control"
                            type="text"
                            placeholder="Phone Number"
                            id="phone"
                            name="phone"
                            required
                          />
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="single-form">
                          <input
                            class="form-control"
                            type="text"
                            placeholder="Subject"
                            id="subject"
                            name="subject"
                            required
                          />
                        </div>
                      </div>
                      <div class="col-md-12">
                        <div class="single-form">
                          <textarea
                            class="form-control"
                            placeholder="Write A Message"
                            id="message"
                            name="message"
                            required
                          ></textarea>
                        </div>
                        <br />
                      </div>
                      <!-- <br> -->
                      <div
                        style="text-align: center"
                        id="hcaptcha"
                        class="h-captcha"
                        data-sitekey="e51ea17a-264f-446b-998f-3e6c4df4f1d1"
                        required
                      ></div>
                      <input
                        type="hidden"
                        name="redirect"
                        value="https://forms.success.lancolatech.co.ke/"
                      />
                      <div class="col-md-12">
                        <div class="form-btn text-center">
                          <button class="btn" type="submit">
                            Send Message
                          </button>
                        </div>
                      </div>
                    </div>
                  </form>
                </div>
                <!-- </form> -->
              </div>
            </div>
          </div>
        </div>
      </div>

      <iframe
        src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d627.2740674030131!2d35.269247999538734!3d0.5140838068682568!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1781015c5cc8a069%3A0x2a52e9d8fd61ce31!2sLancola%20Tech%20Company%20Limited!5e0!3m2!1sen!2ske!4v1651927795448!5m2!1sen!2ske"
        width="100%"
        height="450"
        style="border: 0"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        title="Lancola Tech Company"
        aria-label="Lancola Tech Company"
      ></iframe>

      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <div class="progress-wrap">
        <svg
          class="progress-circle svg-content"
          width="100%"
          height="100%"
          viewBox="-1 -1 102 102"
        >
          <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
        </svg>
      </div>
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <!-- <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script> -->
    <script src="https://unpkg.com/@popperjs/core@2"></script>
    <!-- <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script> -->
    <!-- JavaScript Bundle with Popper -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
      crossorigin="anonymous"
    ></script>

    <!-- Plugins JS -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.min.js"></script>

    <!-- <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script> -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


@app.route('/data-analytics')
def data_analytics():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>
    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />
  </head>

  <body>
    <div class="main-wrapper">
      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li class="active-menu">
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li class="active-menu">
                      <a href="data-analytics">Data Analytics</a>
                    </li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>
              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <!-- Case Study Start -->
      <div class="section case-study-section-2 section-padding">
        <div class="container">
          <!-- Case Study Wrap Start -->
          <div class="case-study-wrap">
            <div class="section-title text-center">
              <br />
              <br />
              <br />
              <h3 class="sub-title">Data Analytics</h3>
              <h4>
                At Lancolatech we examine your company's operating environment,
                domain-specifics, performance, data sources, obstacles, and
                objectives. Our team of talented engineers and business analysts
                strategizes to offer you the solutions that solve your problems
                and propel your company to new heights.
              </h4>
            </div>
          </div>
        </div>
      </div>
      <!-- Case Study End -->

      <div class="section about-section section-padding">
        <div class="container">
          <!-- About Wrap Start -->
          <div class="about-wrap">
            <div class="row">
              <div class="col-lg-6">
                <!-- About Thumb Wrap Start -->
                <div class="about-thumb-wrap">
                  <div class="about-thumb-small">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/pixlr-bg-result234.png"
                      alt=""
                      height="250"
                    />
                  </div>
                  <div class="about-thumb-big">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/clipart1515675.png"
                      alt=""
                      height="265"
                      width="300"
                    />
                  </div>
                  <div class="about-thumb-shape">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/ab-shape.png"
                      alt=""
                    />
                  </div>
                </div>
                <!-- About Thumb Wrap End -->
              </div>
              <div class="col-lg-6">
                <!-- About Content Start -->
                <div class="about-content">
                  <div class="section-title">
                    <h3 class="sub-title">Data Analytics</h3>
                    <h4>
                      We combine data into representations that are optimized
                      for processing and storage. Standardization, handling
                      missing numbers, filtering outliers, and other processes,
                      such as those particular to textual or visual information,
                      are all included in preparation. We gather business data
                      and convert it into a format that can be processed by the
                      available smart solutions.
                    </h4>
                  </div>
                  <p>
                    Data science technologies and cloud computing services like
                    AWS, Azure, and Google Cloud are used. Using tools
                    (databases, containerization, web frameworks, etc.) relevant
                    for the use case, we are prepared to build a customized
                    system based on Python Scientific and ML Stack and integrate
                    it into the client's business infrastructure if the latter
                    wants an on-premise solution.
                  </p>
                  <br />
                  <br />
                </div>
                <!-- About Content End -->
              </div>
            </div>
          </div>
          <!-- About Wrap End -->
        </div>
      </div>
      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <div class="progress-wrap">
        <svg
          class="progress-circle svg-content"
          width="100%"
          height="100%"
          viewBox="-1 -1 102 102"
        >
          <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
        </svg>
      </div>
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


@app.route('/digital-marketing')
def digital_marketing():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>

    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- <link rel="stylesheet" href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/vendor/plugins.min.css">
        <link rel="stylesheet" href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.min.css"> -->
  </head>

  <body>
    <div class="main-wrapper">
      <!-- Preloader start -->
      <!-- <div id="preloader">
            <div class="preloader">
                <span></span>
                <span></span>
            </div>
        </div> -->
      <!-- Preloader End -->

      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li class="active-menu">
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li class="active-menu">
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <!-- Header Search Start -->
              <!-- Header Search End -->

              <!-- Header Cart Start -->

              <!-- Header Cart End -->
              <!-- Header Info Start -->
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>

              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <!-- Case Study Start -->
      <div class="section case-study-section-2 section-padding">
        <div class="container">
          <!-- Case Study Wrap Start -->
          <div class="case-study-wrap">
            <div class="section-title text-center">
              <br />
              <br />
              <br />
              <h3 class="sub-title">Digital Marketing</h3>
              <h4>
                To achieve your business goals, you need an online presence.
                Lancolatech Company is well-equipped to handle these tasks by
                branding your business, growing customer engagement and
                increasing customer engagement. Our team of social media experts
                will help you increase your visibility on popular networks such
                as Facebook, Twitter and Instagram with clever content, targeted
                followers, and strategic engagement opportunities designed to
                drive leads from customers to your business or organization’s
                doorstep!
              </h4>
            </div>
          </div>
          <!-- Case Study Wrap End -->
        </div>
      </div>
      <!-- Case Study End -->

      <div class="section about-section section-padding">
        <div class="container">
          <!-- About Wrap Start -->
          <div class="about-wrap">
            <div class="row">
              <div class="col-lg-6">
                <!-- About Thumb Wrap Start -->
                <div class="about-thumb-wrap">
                  <div class="about-thumb-small">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/Digital-Marketing.jpg"
                      alt=""
                      height="250"
                    />
                  </div>
                  <div class="about-thumb-big">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/pixlr-bg-result (5).png"
                      alt=""
                      height="225"
                      width="300"
                    />
                  </div>
                  <div class="about-thumb-shape">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/ab-shape.png"
                      alt=""
                    />
                  </div>
                  <!-- <div class="play-btn">
                                    <a class="popup-video" href="https://www.youtube.com/watch?time_continue=3&v=_X0eYtY8T_U"><i class="fas fa-play"></i></a>
                                </div> -->
                </div>
                <!-- About Thumb Wrap End -->
              </div>
              <div class="col-lg-6">
                <!-- About Content Start -->
                <div class="about-content">
                  <div class="section-title">
                    <h3 class="sub-title">digital marketing</h3>
                    <h4>
                      We offer digital marketing at an Affordable market price.
                      We do market :
                    </h4>
                  </div>
                  <p>
                    <strong> Businesses </strong>
                    <br />
                    <strong> Institutions </strong>
                    <br />
                    <strong> Events </strong>
                    <br />
                    <strong> Personalities </strong>
                    <br />
                    <strong> products and Services </strong>
                  </p>
                  <br />
                  <br />
                  <br />
                </div>
                <!-- About Content End -->
              </div>
            </div>
          </div>
          <!-- About Wrap End -->
        </div>
      </div>
      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <div class="progress-wrap">
        <svg
          class="progress-circle svg-content"
          width="100%"
          height="100%"
          viewBox="-1 -1 102 102"
        >
          <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
        </svg>
      </div>
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


@app.route('/graphics-design')
def graphics_design():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>
    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />
  </head>

  <body>
    <div class="main-wrapper">
      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li class="active-menu">
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li class="active-menu">
                      <a href="graphics-design">graphics Design</a>
                    </li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>
              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <!-- Case Study Start -->
      <div class="section case-study-section-2 section-padding">
        <div class="container">
          <!-- Case Study Wrap Start -->
          <div class="case-study-wrap">
            <div class="section-title text-center">
              <br />
              <br />
              <br />
              <h3 class="sub-title">graphics design</h3>
              <h4>
                We are a graphic design company based in Eldoret and we offer
                the best products and service. Our services include Logo Design,
                Business Card Design, Photo-hanging, Signage and Lettering, Menu
                Cards and Menu Designs, Corporate Identity Design
              </h4>
            </div>
          </div>
        </div>
      </div>
      <!-- Case Study End -->

      <div class="section about-section section-padding">
        <div class="container">
          <!-- About Wrap Start -->
          <div class="about-wrap">
            <div class="row">
              <div class="col-lg-6">
                <!-- About Thumb Wrap Start -->
                <div class="about-thumb-wrap">
                  <div class="about-thumb-small">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/pixlr-bg-result234.png"
                      alt=""
                      height="250"
                    />
                  </div>
                  <div class="about-thumb-big">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/clipart1515675.png"
                      alt=""
                      height="265"
                      width="300"
                    />
                  </div>
                  <div class="about-thumb-shape">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/ab-shape.png"
                      alt=""
                    />
                  </div>
                  <!-- <div class="play-btn">
                                    <a class="popup-video" href="https://www.youtube.com/watch?time_continue=3&v=_X0eYtY8T_U"><i class="fas fa-play"></i></a>
                                </div> -->
                </div>
                <!-- About Thumb Wrap End -->
              </div>
              <div class="col-lg-6">
                <!-- About Content Start -->
                <div class="about-content">
                  <div class="section-title">
                    <h3 class="sub-title">graphics design</h3>
                    <h4>
                      We offer the best graphics design in Eldoret and are known
                      as a dedicated graphic designer in Kenya. We deliver
                      designs that achieve your goals and our designs cater to
                      all educational needs, business needs, corporate branding
                      and more.
                    </h4>
                  </div>
                  <p>
                    Lancolatech is the best in graphics design and advertising.
                    Our team of expert graphic designers will help you create
                    stunning designs that will be sure to impress.
                  </p>
                  <br />
                  <br />
                  <br />
                  <br />
                </div>
                <!-- About Content End -->
              </div>
            </div>
          </div>
          <!-- About Wrap End -->
        </div>
      </div>
      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <div class="progress-wrap">
        <svg
          class="progress-circle svg-content"
          width="100%"
          height="100%"
          viewBox="-1 -1 102 102"
        >
          <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
        </svg>
      </div>
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


@app.route('/management-systems')
def management_systems():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>

    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />

    <style>
      .pop-out {
        transition: transform 0.5s;
      }

      .pop-out:hover {
        -ms-transform: scale(2, 2);
        -webkit-transform: scale(2, 2);
        transform: scale(2, 2);
      }
    </style>
  </head>

  <body>
    <div class="main-wrapper">
      <!-- Preloader start -->
      <!-- <div id="preloader">
            <div class="preloader">
                <span></span>
                <span></span>
            </div>
        </div> -->
      <!-- Preloader End -->

      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li class="active-menu">
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li class="active-menu">
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <!-- Header Search Start -->
              <!-- Header Search End -->

              <!-- Header Cart Start -->

              <!-- Header Cart End -->
              <!-- Header Info Start -->
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>

              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <!-- Case Study Start -->
      <!-- style="background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/c-study-bg.jpg);" -->
      <!-- To down div -->
      <div class="section case-study-section-2 section-padding">
        <div class="container">
          <!-- Case Study Wrap Start -->
          <div class="case-study-wrap">
            <div class="section-title text-center">
              <br />
              <br />
              <br />
              <!-- <br> -->
              <h3 class="sub-title">management systems</h3>
              <h4>
                LANCOLATECH is a top-of-the line of management systems provider,
                working as the primary tool to give you hope and happiness in
                your business. With our Management System, we provide you with
                easy-to-use tools for all your work structures. With one of the
                leading systems in the company, you can easily and quickly
                develop and integrate structuring within marketing, accounting
                or human resources. Our company is known for its outstanding
                performance in provision of C-POS, C-MED, C-DENT management
                systems across the country.
              </h4>
            </div>
            <!-- Case Study Content Wrap Start -->
            <div class="case-study-content-wrap">
              <div class="row">
                <div class="col-lg-4 col-md-6">
                  <!-- Case Study Item Start -->
                  <div class="case-study-item">
                    <div class="case-study-img">
                      <!-- <a href="https://c-pos.co.ke"> -->
                      <img
                        class="pop-out"
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/CPOS-LANC.png"
                        alt=""
                      />
                      <!-- </a> -->
                    </div>
                    <div class="case-study-content">
                      <div class="header-logo">
                        <a href="/"
                          ><img
                            src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-pointofsell.png"
                            alt=""
                            height="40"
                            width="120"
                        /></a>
                        <br />
                        <br />
                        <h5>Shop, Phamarcy Point of Sale System</h5>
                      </div>
                      <!--   <h3 class="title"><a href="https://c-pos.co.ke" class="fa-solid fa-up-right-from-square" target="_blank"> C-pos</a></h3> -->
                      <!-- <span>Point of sale system</span> -->
                    </div>
                  </div>
                  <div class="case-study-item">
                    <div class="case-study-img">
                      <!-- <a href="https://c-pos.co.ke"> -->
                      <img
                        class="pop-out"
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/C-FIRM SCREEN SHOT.PNG"
                        alt=""
                      />
                      <!-- </a> -->
                    </div>
                    <div class="case-study-content">
                      <div class="header-logo">
                        <a href="/"
                          ><img
                            src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/C-Firm.png"
                            alt=""
                            height="40"
                            width="120"
                        /></a>
                        <br />
                        <br />
                        <h5>Law Firm Management System</h5>
                      </div>
                      <!--   <h3 class="title"><a href="https://c-pos.co.ke" class="fa-solid fa-up-right-from-square" target="_blank"> C-pos</a></h3> -->
                      <!-- <span>Point of sale system</span> -->
                    </div>
                  </div>
                  <!-- Case Study Item End -->
                </div>
                <div class="col-lg-4 col-md-6">
                  <!-- Case Study Item Start -->
                  <div class="case-study-item">
                    <div class="case-study-img">
                      <!-- <a href="https://c-dent.co.ke"> -->
                      <img
                        class="pop-out"
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/C-DENT-LANC.png"
                        alt=""
                      />
                      <!-- </a> -->
                    </div>
                    <div class="case-study-content">
                      <div class="header-logo">
                        <a href="/"
                          ><img
                            src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/C-Dent.png"
                            alt=""
                            height="40"
                            width="120"
                        /></a>
                        <br />
                        <br />
                        <h5>Dental Management System</h5>
                      </div>
                      <!-- <h3 class="title"><a href="https://c-dent.co.ke" class="fa-solid fa-up-right-from-square" target="_blank"> C-dent</a></h3>
                                        <span>Dental clinic system</span> -->
                    </div>
                  </div>
                  <div class="case-study-item">
                    <div class="case-study-img">
                      <!-- <a href="https://c-dent.co.ke"> -->
                      <img
                        class="pop-out"
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/C-EYE SCREEN SHOT.PNG"
                        alt=""
                      />
                      <!-- </a> -->
                    </div>
                    <div class="case-study-content">
                      <div class="header-logo">
                        <a href="/"
                          ><img
                            src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-eye.jpeg"
                            alt=""
                            height="40"
                            width="120"
                        /></a>
                        <br />
                        <br />
                        <h5>Eye clinic Management System</h5>
                      </div>
                      <!-- <h3 class="title"><a href="https://c-dent.co.ke" class="fa-solid fa-up-right-from-square" target="_blank"> C-dent</a></h3>
                                        <span>Dental clinic system</span> -->
                    </div>
                  </div>
                  <!-- Case Study Item End -->z
                </div>
                <div class="col-lg-4 col-md-6">
                  <!-- Case Study Item Start -->
                  <div class="case-study-item">
                    <div class="case-study-img">
                      <!-- <a href="https://c-med.co.ke"> -->
                      <img
                        class="pop-out"
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/CMED-LANCOLA.png"
                        alt=""
                      />
                    </div>
                    <div class="case-study-content">
                      <div class="header-logo">
                        <a href="/"
                          ><img
                            src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-medical.png"
                            alt=""
                            height="40"
                            width="120"
                        /></a>
                        <br />
                        <br />
                        <h5>Hospital/Medical Management System</h5>
                      </div>
                      <!-- <h3 class="title"><a href="https://c-med.co.ke" class="fa-solid fa-up-right-from-square" target="_blank"> C-med</a></h3>
                                        <span>Medical facility system</span> -->
                    </div>
                  </div>
                  <!-- Case Study Item End -->
                  <div class="case-study-item">
                    <div class="case-study-img">
                      <!-- <a href="https://c-med.co.ke"> -->
                      <img
                        class="pop-out"
                        src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/schoolsys.png"
                        alt=""
                      />
                    </div>
                    <div class="case-study-content">
                      <div class="header-logo">
                        <!-- <a href="/"
                          ><img
                            src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-medical.png"
                            alt=""
                            height="40"
                            width="120"
                        /></a> -->
                        <br />
                        <br />
                        <h5>University/college/school Managements System</h5>
                      </div>
                      <!-- <h3 class="title"><a href="https://c-med.co.ke" class="fa-solid fa-up-right-from-square" target="_blank"> C-med</a></h3>
                                        <span>Medical facility system</span> -->
                    </div>
                  </div>
                  <!-- Case Study Item End -->
                </div>
              </div>
            </div>
            <!-- Case Study Content Wrap End -->
          </div>
          <!-- Case Study Wrap End -->
        </div>
      </div>
      <!-- Case Study End -->

      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <div class="progress-wrap">
        <svg
          class="progress-circle svg-content"
          width="100%"
          height="100%"
          viewBox="-1 -1 102 102"
        >
          <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
        </svg>
      </div>
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- fontawesome -->
    <script
      src="https://kit.fontawesome.com/ecc9374992.js"
      crossorigin="anonymous"
    ></script>

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


@app.route('/pricing')
def pricing():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>
    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <!-- <link rel="stylesheet" href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/price.css"> -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"> -->
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css"> -->
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"> -->
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />
  </head>
  <body>
    <div class="main-wrapper">
      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li>
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li class="active-menu"><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <!-- Header Search Start -->
              <!-- Header Search End -->

              <!-- Header Cart Start -->

              <!-- Header Cart End -->
              <!-- Header Info Start -->
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>

              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <div class="section case-study-section-2 section-padding">
        <div class="container">
          <div class="case-study-wrap">
            <div class="section-title text-center">
              <br />
              <br />
              <br />
              <h3 class="sub-title">web development</h3>
            </div>
          </div>
        </div>
      </div>

      <div class="section pricing-section pricing-section-2 section-padding-02">
        <div class="container">
          <div class="pricing-wrap">
            <div class="section-title2 text-center">
              <h2>Small and medium-sized enterprises</h2>
              <h4 class="title">
                <span><strong>pricing</strong></span>
              </h4>
              <p>
                Accelerate innovation with world-class tech teams We’ll match
                you to an entire remote team of incredible freelance talent.
              </p>
            </div>
            <div class="pricing-content-wrap">
              <div class="row">
                <div class="col-xl-4 col-md-6">
                  <div class="single-pricing">
                    <div class="pricing-badge">
                      <span class="title">Bronze</span>
                    </div>
                    <div class="pricing-price">
                      <span class="price">18,999</span>
                      <span class="currency">Kshs</span>
                    </div>
                    <div class="pricing-content">
                      <ul class="pricing-list">
                        <li>
                          <i class="fas fa-check"></i> Social Media Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Google Maps Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li><i class="fas fa-check"></i> 6 Pages Maximum</li>
                        <li><i class="fas fa-check"></i> Contact Form</li>
                        <li>
                          <i class="fas fa-check"></i> Basic Search Engine
                          Optimization
                        </li>
                      </ul>
                      <div class="pricing-btn">
                        <a class="btn" href="mailto:info@lancolatech.co.ke"
                          >Get Started</a
                        >
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-md-6">
                  <div class="single-pricing active">
                    <div class="pricing-badge">
                      <span class="title">Silver</span>
                    </div>
                    <div class="pricing-price">
                      <span class="price">21,999</span>
                      <span class="currency">Kshs</span>
                    </div>
                    <div class="pricing-content">
                      <ul class="pricing-list">
                        <li>
                          <i class="fas fa-check"></i> Social Media Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Google Maps Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li><i class="fas fa-check"></i> 8 Pages Maximum</li>
                        <li>
                          <i class="fas fa-check"></i> Contact Form and feedback
                          forms
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Basic Search Engine
                          Optimization
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Basic Database
                          Integration
                        </li>
                      </ul>
                      <div class="pricing-btn">
                        <a class="btn" href="mailto:info@lancolatech.co.ke"
                          >Get Started</a
                        >
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-md-6">
                  <div class="single-pricing">
                    <div class="pricing-badge">
                      <span class="title">Gold</span>
                      <span class="recommend">Recommended</span>
                    </div>
                    <div class="pricing-price">
                      <span class="price">26,999</span>
                      <span class="currency">Kshs</span>
                    </div>
                    <div class="pricing-content">
                      <ul class="pricing-list">
                        <li>
                          <i class="fas fa-check"></i> Social Media Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Google Maps Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li><i class="fas fa-check"></i> 10 Pages Maximum</li>
                        <li>
                          <i class="fas fa-check"></i> Contact Form and feedback
                          forms
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Advanced Search Engine
                          Optimization
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Basic Database
                          Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Back End Development
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Artistic Design and
                          Website layout
                        </li>
                        <li><i class="fas fa-check"></i> Easy navigation</li>
                        <li>
                          <i class="fas fa-check"></i> Live Chat System
                          Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Captcha for spam
                          prevention
                        </li>
                      </ul>
                      <div class="pricing-btn">
                        <a class="btn" href="mailto:info@lancolatech.co.ke"
                          >Get Started</a
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- BULK SMS PRICING -->
      <div class="section case-study-section-2 section-padding">
        <div class="container">
          <div class="case-study-wrap">
            <div class="section-title text-center">
              <br />
              <br />
              <br />
              <h3 class="sub-title">bulk sms</h3>
            </div>
          </div>
        </div>
      </div>

      <div class="section pricing-section pricing-section-2 section-padding-02">
        <div class="container">
          <div class="pricing-wrap">
            <div class="section-title2 text-center">
              <h2>SME's and Corporate Clients</h2>
              <h4 class="title">
                <!-- <span><strong>pricing</strong></span> -->
              </h4>
              <!-- <p>
                Accelerate innovation with world-class tech teams We’ll match
                you to an entire remote team of incredible freelance talent.
              </p> -->
            </div>
            <div class="pricing-content-wrap">
              <div class="row">
                <div class="col-xl-4 col-md-6">
                  <div class="single-pricing">
                    <div class="pricing-badge">
                      <span class="title">SME's</span>
                    </div>
                    <div class="pricing-price">
                      <span class="price">14,000</span>
                      <span class="currency">Kshs</span>
                    </div>
                    <div class="pricing-content">
                      <!-- <ul class="pricing-list">
                        <li>
                          <i class="fas fa-check"></i> Social Media Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Google Maps Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li><i class="fas fa-check"></i> 6 Pages Maximum</li>
                        <li><i class="fas fa-check"></i> Contact Form</li>
                        <li>
                          <i class="fas fa-check"></i> Basic Search Engine
                          Optimization
                        </li>
                      </ul> -->
                      <div class="pricing-btn">
                        <a class="btn" href="mailto:info@lancolatech.co.ke"
                          >Get Started</a
                        >
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-md-6">
                  <div class="single-pricing active">
                    <div class="pricing-badge">
                      <span class="title">Corporate</span>
                    </div>
                    <div class="pricing-price">
                      <span class="price">25,000</span>
                      <span class="currency">Kshs</span>
                    </div>
                    <div class="pricing-content">
                      <!-- <ul class="pricing-list">
                        <li>
                          <i class="fas fa-check"></i> Social Media Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Google Maps Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li><i class="fas fa-check"></i> 8 Pages Maximum</li>
                        <li>
                          <i class="fas fa-check"></i> Contact Form and feedback
                          forms
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Basic Search Engine
                          Optimization
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Basic Database
                          Integration
                        </li>
                      </ul> -->
                      <div class="pricing-btn">
                        <a class="btn" href="mailto:info@lancolatech.co.ke"
                          >Get Started</a
                        >
                      </div>
                    </div>
                  </div>
                </div>
                <!-- <div class="col-xl-4 col-md-6">
                  <div class="single-pricing">
                    <div class="pricing-badge">
                      <span class="title">Gold</span>
                      <span class="recommend">Recommended</span>
                    </div>
                    <div class="pricing-price">
                      <span class="price">26,999</span>
                      <span class="currency">Kshs</span>
                    </div>
                    <div class="pricing-content">
                      <ul class="pricing-list">
                        <li>
                          <i class="fas fa-check"></i> Social Media Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Google Maps Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li><i class="fas fa-check"></i> 10 Pages Maximum</li>
                        <li>
                          <i class="fas fa-check"></i> Contact Form and feedback
                          forms
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Advanced Search Engine
                          Optimization
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Basic Database
                          Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Back End Development
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Artistic Design and
                          Website layout
                        </li>
                        <li><i class="fas fa-check"></i> Easy navigation</li>
                        <li>
                          <i class="fas fa-check"></i> Live Chat System
                          Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Captcha for spam
                          prevention
                        </li>
                      </ul>
                      <div class="pricing-btn">
                        <a class="btn" href="mailto:info@lancolatech.co.ke"
                          >Get Started</a
                        >
                      </div>
                    </div>
                  </div>
                </div> -->
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Pricing End -->
      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <div class="progress-wrap">
        <svg
          class="progress-circle svg-content"
          width="100%"
          height="100%"
          viewBox="-1 -1 102 102"
        >
          <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
        </svg>
      </div>
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


@app.route('/structured-cabling-and-networking')
def structured_cabling_and_networking():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>

    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- <link rel="stylesheet" href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/vendor/plugins.min.css">
        <link rel="stylesheet" href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.min.css"> -->
  </head>

  <body>
    <div class="main-wrapper">
      <!-- Preloader start -->
      <!-- <div id="preloader">
            <div class="preloader">
                <span></span>
                <span></span>
            </div>
        </div> -->
      <!-- Preloader End -->

      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li class="active-menu">
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li class="active-menu">
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li><a href="web-development">Web Development</a></li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <!-- Header Search Start -->
              <!-- Header Search End -->

              <!-- Header Cart Start -->

              <!-- Header Cart End -->
              <!-- Header Info Start -->
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>

              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <!-- Case Study Start -->
      <div class="section case-study-section-2 section-padding">
        <div class="container">
          <!-- Case Study Wrap Start -->
          <div class="case-study-wrap">
            <div class="section-title text-center">
              <br />
              <br />
              <br />
              <h3 class="sub-title">structured cabling and networking</h3>
              <h4>
                Lancolatech Company is a known supplier of structured cable and
                networking services. We offer network cables, systems, and
                solutions that meet the highest industry specifications; form
                factors that fit their customers' requirements; with exceptional
                performance and reliability in network, power and structured
                cabling. Lancolatech's structured cabling solutions are built
                around its network policy that confirm with industrial
                standards, which enables it to deliver end-to-end solutions that
                integrate from design to installation, from component sourcing
                and assembly to installation procedures. Lancolatech's modular
                approach to networking makes it straightforward for other
                companies to participate in our value chain.
              </h4>
            </div>
            <!-- Case Study Content Wrap Start -->
            <!-- <div class="case-study-content-wrap">
                        <div class="row">
                            <div class="col-lg-4 col-md-6">
                                <div class="case-study-item">
                                    <div class="case-study-img">
                                        <a href="#"><img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-study-4.jpg" alt=""></a>
                                    </div>
                                    <div class="case-study-content">
                                        <h3 class="title"><a href="#">C-pos</a></h3>
                                        <span>Point of sale system</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6">
                                <div class="case-study-item">
                                    <div class="case-study-img">
                                        <a href="#"><img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-study-5.jpg" alt=""></a>
                                    </div>
                                    <div class="case-study-content">
                                        <h3 class="title"><a href="#">C-dent</a></h3>
                                        <span>Dental clinic system</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6">
                                <div class="case-study-item">
                                    <div class="case-study-img">
                                        <a href="#"><img src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/c-study-6.jpg" alt=""></a>
                                    </div>
                                    <div class="case-study-content">
                                        <h3 class="title"><a href="#">C-med</a></h3>
                                        <span>Medical facility system</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div> -->
            <!-- Case Study Content Wrap End -->
          </div>
          <!-- Case Study Wrap End -->
        </div>
        <!-- <div class="section-title text-center">
                        <br>
                        <h3>Lancolatech Company is a known supplier of structured cable and networking services. We offer network cables, systems, and solutions that meet the highest industry specifications; form factors that fit their customers' requirements; with exceptional performance and reliability in network, power and structured cabling. Lancolatech's structured cabling solutions are built around its network policy that confirm with industrial standards, which enables it to deliver end-to-end solutions that integrate from design to installation, from component sourcing and assembly to installation procedures. Lancolatech's modular approach to networking makes it straightforward for other companies to participate in our value chain.</h3>
                    </div> -->
      </div>
      <!-- Case Study End -->

      <div class="section about-section section-padding">
        <div class="container">
          <!-- About Wrap Start -->
          <div class="about-wrap">
            <div class="row">
              <div class="col-lg-6">
                <!-- About Thumb Wrap Start -->
                <div class="about-thumb-wrap">
                  <div class="about-thumb-small">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/pixlr-bg-result98656.png"
                      alt=""
                      height="300"
                    />
                  </div>
                  <div class="about-thumb-big">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/pixlr-bg-result (3).png"
                      alt=""
                      height="270"
                      width="270"
                    />
                  </div>
                  <div class="about-thumb-shape">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/ab-shape.png"
                      alt=""
                    />
                  </div>
                </div>
                <!-- About Thumb Wrap End -->
              </div>
              <div class="col-lg-6">
                <!-- About Content Start -->
                <div class="about-content">
                  <div class="section-title">
                    <h3 class="sub-title">Structured Cabling and Networking</h3>
                    <h4>
                      Structured cabling is critical backbone that drives todays
                      communication systesms.
                    </h4>
                  </div>
                  <p>
                    Our teams of expert at LancolaTech designs and installs cost
                    effective communications systems built and customized to
                    meet the requirements and demands of your growing business.
                  </p>
                  <br />
                  <br />
                  <br />
                </div>
                <!-- About Content End -->
              </div>
            </div>
          </div>
          <!-- About Wrap End -->
        </div>
      </div>

      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <div class="progress-wrap">
        <svg
          class="progress-circle svg-content"
          width="100%"
          height="100%"
          viewBox="-1 -1 102 102"
        >
          <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
        </svg>
      </div>
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!--====== Use the minified version files listed below for better performance and remove the files listed above ======-->
    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


@app.route('/web-development')
def web_development():
    page = """<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Lancolatech Company Limited</title>

    <meta name="description" content="" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <!-- Favicon -->
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/favi.png"
    />
    <!-- Icon Font CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/all.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/flaticon.css"
    />
    <!-- Plugins CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/bootstrap.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/swiper-bundle.min.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/aos.css"
    />
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/plugins/magnific-popup.css"
    />
    <!-- <link rel="stylesheet" href="https://cdn.owino.xyz/pace/flash.css"> -->
    <!-- Main Style CSS -->
    <link
      rel="stylesheet"
      href="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/css/style.css"
    />
  </head>

  <body>
    <div class="main-wrapper">
      <!-- Preloader start -->
      <!-- <div id="preloader">
            <div class="preloader">
                <span></span>
                <span></span>
            </div>
        </div> -->
      <!-- Preloader End -->

      <!-- Header Start  -->
      <div
        id="header"
        class="section header-section header-section-2 transparent-header"
      >
        <div class="container">
          <!-- Header Wrap Start  -->
          <div class="header-wrap">
            <div class="header-logo">
              <a href="/"
                ><img
                  src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                  alt=""
              /></a>
            </div>

            <div class="header-menu header-menu-2 d-none d-lg-block">
              <ul class="main-menu">
                <li>
                  <a href="/">Home</a>
                </li>
                <li>
                  <a href="about">About Us</a>
                </li>
                <li class="active-menu">
                  <a href="javascript:;">Our Services</a>
                  <ul class="sub-menu">
                    <li><a href="bulk-sms">Bulk SMS</a></li>
                    <li>
                      <a href="management-systems">Management Systems</a>
                    </li>
                    <!-- <li><a href="computer-solutions-and-consultancy">Computer Solutions & Consultancy</a></li> -->
                    <li>
                      <a href="computer-accessories"
                        >Computer Accessories</a
                      >
                    </li>
                    <li>
                      <a href="CCTV-installations">CCTV Installtions</a>
                    </li>
                    <li>
                      <a href="structured-cabling-and-networking"
                        >Structured Cabling & Networking</a
                      >
                    </li>
                    <li>
                      <a href="digital-marketing">Digital Marketing</a>
                    </li>
                    <li class="active-menu">
                      <a href="web-development">Web Development</a>
                    </li>
                    <li>
                      <a href="computer-solutions-and-consultancy"
                        >Computer Solutions & Consultancy</a
                      >
                    </li>
                    <li><a href="data-analytics">Data Analytics</a></li>
                    <li><a href="graphics-design">graphics Design</a></li>
                  </ul>
                </li>
                <li><a href="pricing">Pricing</a></li>
                <li>
                  <a href="https://blog.lancolatech.co.ke" target="_blank"
                    >Blog</a
                  >
                </li>
                <li><a href="contact">Contact</a></li>
              </ul>
            </div>

            <!-- Header Meta Start -->
            <div class="header-meta">
              <!-- Header Search Start -->
              <!-- Header Search End -->

              <!-- Header Cart Start -->

              <!-- Header Cart End -->
              <!-- Header Info Start -->
              <div class="header-info d-none d-md-flex">
                <div class="info-icon">
                  <i class="fas fa-phone-alt"></i>
                </div>
                <div class="info-text">
                  <span>For Enquiries</span>
                  <span class="number"
                    ><a href="tel:254115588872">+254 115 588 872</a></span
                  >
                  <span class="number"
                    ><a href="tel:254715223428">+254 715 223 428</a></span
                  >
                </div>
              </div>
              <!-- Header Info End -->
              <div class="header-btn-2 d-none d-xl-block">
                <a class="btn" href="mailto:info@lancolatech.co.ke"
                  >Email Us!</a
                >
              </div>
              <!-- Header Toggle Start -->
              <div class="header-toggle d-lg-none">
                <button
                  data-bs-toggle="offcanvas"
                  data-bs-target="#offcanvasExample"
                >
                  <span></span>
                  <span></span>
                  <span></span>
                </button>
              </div>
              <!-- Header Toggle End -->
            </div>
            <!-- Header Meta End  -->
          </div>
          <!-- Header Wrap End  -->
        </div>
      </div>
      <!-- Header End -->

      <!-- Offcanvas Start-->
      <div class="offcanvas offcanvas-start" id="offcanvasExample">
        <div class="offcanvas-header">
          <!-- Offcanvas Logo Start -->
          <div class="offcanvas-logo">
            <a href="/"
              ><img
                src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo-white.png"
                alt=""
            /></a>
          </div>
          <!-- Offcanvas Logo End -->
          <button type="button" class="close-btn" data-bs-dismiss="offcanvas">
            <i class="flaticon-close"></i>
          </button>
        </div>

        <!-- Offcanvas Body Start -->
        <div class="offcanvas-body">
          <div class="offcanvas-menu">
            <ul class="main-menu">
              <li class="active-menu">
                <a href="/">Home</a>
              </li>
              <li>
                <a href="about">About Us</a>
              </li>
              <li>
                <a href="javascript:;">Our Services</a>
                <ul class="sub-menu">
                  <li><a href="bulk-sms">Bulk SMS</a></li>
                  <li>
                    <a href="management-systems">Management Systems</a>
                  </li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                  <li>
                    <a href="computer-accessories">Computer Accessories</a>
                  </li>
                  <li>
                    <a href="CCTV-installations">CCTV Installtions</a>
                  </li>
                  <li>
                    <a href="structured-cabling-and-networking"
                      >Structured Cabling and Networking</a
                    >
                  </li>
                  <li>
                    <a href="digital-marketing">Digital Marketing</a>
                  </li>
                  <li><a href="web-development">Web Development</a></li>
                  <li>
                    <a href="computer-solutions-and-consultancy"
                      >Computer Solutions & Consultancy</a
                    >
                  </li>
                </ul>
              </li>
              <li>
                <a href="https://blog.lancolatech.co.ke" target="_blank"
                  >Blog</a
                >
              </li>

              <li><a href="contact">Contact</a></li>
            </ul>
          </div>
        </div>
        <!-- Offcanvas Body End -->
      </div>
      <!-- Offcanvas End -->

      <!-- Case Study Start -->
      <div class="section case-study-section-2 section-padding">
        <div class="container">
          <div class="case-study-wrap">
            <div class="section-title text-center">
              <br />
              <br />
              <br />
              <h3 class="sub-title">web development</h3>
              <h4>
                We offer custom web development services, from simple, elegant
                designs for small businesses to complex websites for large
                enterprises. Our experienced team can create a new website from
                scratch or help you evolve an existing site by redesigning it.
                We offer affordable rates, and we use cutting-edge software that
                will ensure your projects are optimized for high search engine
                rankings and responsive to mobile phones and all screen sizes.
              </h4>
            </div>
          </div>
        </div>
      </div>

      <div class="section about-section section-padding">
        <div class="container">
          <!-- About Wrap Start -->
          <div class="about-wrap">
            <div class="row">
              <div class="col-lg-6">
                <!-- About Thumb Wrap Start -->
                <div class="about-thumb-wrap">
                  <div class="about-thumb-small">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/pexels-kevin-ku-577585.jpg"
                      alt=""
                      height="250"
                    />
                  </div>
                  <div class="about-thumb-big">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/service/pixlr-bg-result (4).png"
                      alt=""
                      height="265"
                      width="400"
                    />
                  </div>
                  <div class="about-thumb-shape">
                    <img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/ab-shape.png"
                      alt=""
                    />
                  </div>
                </div>
                <!-- About Thumb Wrap End -->
              </div>
              <div class="col-lg-6">
                <!-- About Content Start -->
                <div class="about-content">
                  <div class="section-title">
                    <h3 class="sub-title">Web Development</h3>
                    <h4>
                      We offer a world class web development service to our
                      clients.Our services are unique and up to date with the
                      current state of art technologies.
                    </h4>
                  </div>
                  <p>
                    LancolaTech company has talented web designers and
                    programmers and we are trusted by hundreds of clients across
                    the country for whom we have developed the most prestigious,
                    interactive brands. We develop Ecommerce, Enterprise and
                    Small business web applications
                  </p>
                </div>
                <!-- About Content End -->
              </div>
            </div>
          </div>
          <!-- About Wrap End -->
        </div>
      </div>

      <!-- Pricing Start -->
      <div class="section pricing-section pricing-section-2 section-padding-02">
        <div class="container">
          <!-- Pricing Wrap Start -->
          <div class="pricing-wrap">
            <div class="section-title2 text-center">
              <h2>Small and medium-sized enterprises</h2>
              <h4 class="title">
                <span><strong>pricing</strong></span>
              </h4>
              <p>
                Accelerate innovation with world-class tech teams We’ll match
                you to an entire remote team of incredible freelance talent.
              </p>
            </div>
            <!-- Pricing Content Wrap Start -->
            <div class="pricing-content-wrap">
              <div class="row">
                <div class="col-xl-4 col-md-6">
                  <!-- Single Pricing Start -->
                  <div class="single-pricing">
                    <div class="pricing-badge">
                      <span class="title">Bronze</span>
                    </div>
                    <div class="pricing-price">
                      <span class="price">18,999</span>
                      <span class="currency">Kshs</span>
                      <!-- <p>For Smaller <br> Business</p> -->
                    </div>
                    <div class="pricing-content">
                      <ul class="pricing-list">
                        <li>
                          <i class="fas fa-check"></i> Social Media Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Google Maps Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li><i class="fas fa-check"></i> 6 Pages Maximum</li>
                        <li><i class="fas fa-check"></i> Contact Form</li>
                        <li>
                          <i class="fas fa-check"></i> Basic Search Engine
                          Optimization
                        </li>
                      </ul>
                      <div class="pricing-btn">
                        <a class="btn" href="mailto:info@lancolatech.co.ke"
                          >Get Started</a
                        >
                        <!-- <a class="pricing-contact" href="#">Contact Us</a> -->
                      </div>
                    </div>
                  </div>
                  <!-- Single Pricing End -->
                </div>
                <div class="col-xl-4 col-md-6">
                  <!-- Single Pricing Start -->
                  <div class="single-pricing active">
                    <div class="pricing-badge">
                      <span class="title">Silver</span>
                      <!-- <span class="recommend">Recommend</span> -->
                    </div>
                    <div class="pricing-price">
                      <span class="price">21,999</span>
                      <span class="currency">Kshs</span>
                      <!-- <p>For Growth <br> Business</p> -->
                    </div>
                    <div class="pricing-content">
                      <ul class="pricing-list">
                        <li>
                          <i class="fas fa-check"></i> Social Media Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Google Maps Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li><i class="fas fa-check"></i> 8 Pages Maximum</li>
                        <li>
                          <i class="fas fa-check"></i> Contact Form and feedback
                          forms
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Basic Search Engine
                          Optimization
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Basic Database
                          Integration
                        </li>
                      </ul>
                      <div class="pricing-btn">
                        <a class="btn" href="mailto:info@lancolatech.co.ke"
                          >Get Started</a
                        >
                        <!-- <a class="pricing-contact" href="#">Contact Us</a> -->
                      </div>
                    </div>
                  </div>
                  <!-- Single Pricing End -->
                </div>
                <div class="col-xl-4 col-md-6">
                  <!-- Single Pricing Start -->
                  <div class="single-pricing">
                    <div class="pricing-badge">
                      <span class="title">Gold</span>
                      <span class="recommend">Recommended</span>
                    </div>
                    <div class="pricing-price">
                      <span class="price">26,999</span>
                      <span class="currency">Kshs</span>
                      <!-- <p>For Top <br> Business</p> -->
                    </div>
                    <div class="pricing-content">
                      <ul class="pricing-list">
                        <li>
                          <i class="fas fa-check"></i> Social Media Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Google Maps Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li><i class="fas fa-check"></i> 10 Pages Maximum</li>
                        <li>
                          <i class="fas fa-check"></i> Contact Form and feedback
                          forms
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Advanced Search Engine
                          Optimization
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Browser Consistency
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Basic Database
                          Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Back End Development
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Artistic Design and
                          Website layout
                        </li>
                        <li><i class="fas fa-check"></i> Easy navigation</li>
                        <li>
                          <i class="fas fa-check"></i> Live Chat System
                          Integration
                        </li>
                        <li>
                          <i class="fas fa-check"></i> Captcha for spam
                          prevention
                        </li>
                      </ul>
                      <div class="pricing-btn">
                        <a class="btn" href="mailto:info@lancolatech.co.ke"
                          >Get Started</a
                        >
                        <!-- <a class="pricing-contact" href="#">Contact Us</a> -->
                      </div>
                    </div>
                  </div>
                  <!-- Single Pricing End -->
                </div>
              </div>
            </div>
            <!-- Pricing Content Wrap End -->
          </div>
          <!-- Pricing Wrap End -->
        </div>
      </div>
      <!-- Pricing End -->

      <!-- Footer Section Start -->
      <div
        class="section footer-section footer-section-2"
        style="
          background-image: url(https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/bg/footer-bg-2.jpg);
        "
      >
        <div class="container">
          <!-- Footer Widget Wrap Start -->
          <div class="footer-widget-wrap footer-widget-wrap-2">
            <div class="row">
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget-about">
                  <a class="footer-logo" href="/"
                    ><img
                      src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/images/logo.png"
                      alt="Logo"
                  /></a>
                  <div class="widget-info widget-info-2">
                    <ul>
                      <!-- <li>
                                            <div class="info-icon">
                                                <i class="flaticon-phone-call"></i>
                                            </div>
                                            <div class="info-text">
                                                <span><a href="tel:254115588872">+254 115 588 872</a></span>
                                                <span><a href="tel:254715223428">+254 715 223 428</a></span>
                                            </div>
                                        </li> -->
                      <li>
                        <div class="info-icon">
                          <i class="far fa-envelope-open"></i>
                        </div>
                        <div class="info-text">
                          <span
                            ><a href="mailto:info@lancolatech.co.ke"
                              >info@lancolatech.co.ke</a
                            ></span
                          >
                        </div>
                      </li>
                      <li>
                        <div class="info-icon">
                          <i class="flaticon-pin"></i>
                        </div>
                        <div class="info-text">
                          <span>Grand Pri 3rd Floor Room 301, Eldoret</span>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
              <div class="col-lg-3 col-sm-6">
                <!-- Footer Widget Start -->
                <div class="footer-widget footer-widget-2">
                  <h4 class="footer-widget-title">Useful Links</h4>

                  <div class="widget-link">
                    <ul class="link">
                      <li>
                        <a href="terms-and-conditions.txt" target="_blank"
                          >Terms & Conditions</a
                        >
                      </li>
                      <li><a href="https://blog.lancolatech.co.ke">Blog</a></li>
                      <!-- <li><a href="support">Support</a></li> -->
                    </ul>
                  </div>
                </div>
                <!-- Footer Widget End -->
              </div>
            </div>
          </div>
          <!-- Footer Widget Wrap End -->
        </div>

        <!-- Footer Copyright Start -->
        <div class="footer-copyright-area footer-copyright-2">
          <div class="container">
            <div class="footer-copyright-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Text Start -->
                  <div class="copyright-text">
                    <p>
                      <strong>
                        &copy; <span id="copyright-year"></span>
                        <script>
                          document.querySelector("#copyright-year").innerText =
                            new Date().getFullYear();
                        </script>
                        Lancolatech</strong
                      >
                    </p>
                  </div>
                  <!-- Footer Copyright Text End -->
                </div>
                <div class="col-lg-6 col-md-6">
                  <!-- Footer Copyright Social Start -->
                  <div class="copyright-social">
                    <ul class="social">
                      <li>
                        <a
                          href="https://www.facebook.com/Lancola-Tech-246152853989129"
                          target="_blank"
                          ><i class="fab fa-facebook-f"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://twitter.com/lancolatech"
                          ><i class="fab fa-twitter"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://www.instagram.com/lancolatech/"
                          ><i class="fab fa-instagram"></i
                        ></a>
                      </li>
                      <li>
                        <a href="https://linkedin.com/in/lancolatech"
                          ><i class="fab fa-linkedin-in"></i
                        ></a>
                      </li>
                    </ul>
                  </div>
                  <!-- Footer Copyright Social End -->
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Footer Copyright End -->
      </div>
      <!-- Footer Section End -->

      <!-- back to top start -->
      <div class="progress-wrap">
        <svg
          class="progress-circle svg-content"
          width="100%"
          height="100%"
          viewBox="-1 -1 102 102"
        >
          <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
        </svg>
      </div>
      <!-- back to top end -->
    </div>

    <!-- JS
    ============================================ -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/vendor/modernizr-3.11.2.min.js"></script>

    <!-- Bootstrap JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/popper.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/bootstrap.min.js"></script>

    <!-- Plugins JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/swiper-bundle.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/aos.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/waypoints.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/back-to-top.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.counterup.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/appear.min.js"></script>
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/plugins/jquery.magnific-popup.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pace-js@latest/pace.min.js"></script>

    <!-- tawk.to -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/tawk/main.js"></script>

    <!-- Main JS -->
    <script src="https://ver-vite.assets.cdn.lancolatech.co.ke/assets/js/main.js"></script>
  </body>
</html>
"""
    return page


app.run(host='0.0.0.0', port=81)
