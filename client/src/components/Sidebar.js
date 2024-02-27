// Move styles to index.css
import React, { useState } from 'react';
import { Sidebar, SubMenu, Menu, MenuItem } from 'react-pro-sidebar';
import { Link } from 'react-router-dom';
import { useAuth } from 'AuthContext';
// icons
import { FiChevronsLeft, FiChevronsRight } from 'react-icons/fi';
import { FaCode, FaUpload, FaChalkboardTeacher } from 'react-icons/fa';
import { MdOutlineMailOutline } from "react-icons/md";
import { RiAdminLine } from "react-icons/ri";
import { TbLetterS } from "react-icons/tb";

import 'assets/global.css';

function Sidebars({ onCollapsedChange }) {

  const [collapsed, setCollapsed] = useState(false);
  const [toggled, setToggled] = useState(false);

  const { isLoggedIn } = useAuth();

  const handleCollapsedChange = () => {
    setCollapsed(!collapsed);
    onCollapsedChange(!collapsed); // Notify the parent component about the state change
  };
  const handleToggleSidebar = (value) => {
    setToggled(value);
  };

  // TODO: move styles to .css
  return (
    <div style={{ display: "flex" }}>
      <Sidebar
        className={`app ${toggled ? "toggled" : ""}`}
        style={{ height: "100%", position: "fixed", display: "inline-block" }}
        collapsed={collapsed}
        toggled={toggled}
        handleToggleSidebar={handleToggleSidebar}
        handleCollapsedChange={handleCollapsedChange}
      >
        <main>
          <Menu>
            {collapsed ? (
              <MenuItem
                icon={<FiChevronsRight />}
                onClick={handleCollapsedChange}
              ></MenuItem>
            ) : (
              <MenuItem
                suffix={<FiChevronsLeft />}
                onClick={handleCollapsedChange}
                className="menu-item"
              >
                <div className="title">PYTHON TUTOR</div>
              </MenuItem>
            )}
            <hr />
          </Menu>

          <Menu>
            {/* Warning cuz of double <a> can use NavLink, but it breaks submenu */}
            <MenuItem icon={<FaUpload />} component={<Link to="/upload" />}>Upload project</MenuItem>
            <SubMenu defaultOpen label={"Practice"} icon={<FaChalkboardTeacher />}>
              <MenuItem icon={<FaCode />} component={<Link to="/#" />}>Regex</MenuItem>
              <MenuItem icon={<TbLetterS />} component={<Link to="/Proj4" />} >Scrabble</MenuItem>
              <MenuItem icon={<MdOutlineMailOutline />} component={<Link to="/proj8" />} >Email Queue</MenuItem>
            </SubMenu>
          </Menu>

          <div className="menu-bottom">
            <Menu>
              {isLoggedIn ? (
                <>
                  <MenuItem icon={<RiAdminLine />} component={<Link to="/admin" />}>
                    Admin
                  </MenuItem>
                  <MenuItem icon={<RiAdminLine />} /*onClick={logout}*/>
                    Logout
                  </MenuItem>
                </>
              ) : (
                <MenuItem icon={<RiAdminLine />} component={<Link to="/login" />}>
                  Login
                </MenuItem>
              )}
            </Menu>
          </div>
        </main>
      </Sidebar>
    </div>
  );
}
export default Sidebars;
